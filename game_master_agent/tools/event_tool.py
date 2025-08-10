import os
from dotenv import load_dotenv, find_dotenv
from agents import function_tool, RunContextWrapper, AsyncOpenAI
from config import client
from typing_extensions import TypedDict

load_dotenv(find_dotenv())

api_key=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )


class EventOutput(TypedDict, total=False):
    event: str
    phase: str
    message: str
    choices: list[str]


@function_tool
async def generate_event(wrapper: RunContextWrapper, input: EventOutput) -> EventOutput:
    """
    Generate a dynamic game event using the LLM.
    Expects input = {"phase": "<phase>", "location": "<optional>", "last_action": "<optional>"}
    Returns {"event": "<short description>", "phase": "<phase>", "message": "<full text to show player>", "choices": ["opt1","opt2",...]}
    """
    import json
    import re

    try:
        phase = (input.get("phase") or "narration").lower()
        location = input.get("location", "").strip()
        last_action = input.get("last_action", "").strip()

        prompt_parts = [f"Phase: {phase}"]
        if location:
            prompt_parts.append(f"Location: {location}")
        if last_action:
            prompt_parts.append(f"Player action: {last_action}")

        prompt_parts.append(
            "You are a concise game event generator for a text-based fantasy adventure.\n\n"
    "Context: use the provided Phase/Location/Player action to create the next short event.\n\n"
    "OUTPUT REQUIREMENT (VERY STRICT): Return ONLY a single valid JSON object with exactly these keys:\n"
    "  - \"event\": a 1-2 sentence event description (string)\n"
    "  - \"choices\": an array of 2 or 3 short option strings (exact user inputs the player can type)\n\n"
    "Example valid output:\n"
    '{"event":"A hidden chest glints under the roots.","choices":["Approach the chest cautiously","Examine the surrounding area for traps","Leave it and go back"]}\n\n'
    "Do NOT include any extra text, markdown, or commentary outside the JSON. If you cannot generate choices, return \"choices\": [] within the JSON."
        )

        prompt = "\n\n".join(prompt_parts)

        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}],
            # you can add max_tokens or temperature overrides here if desired
        )

        raw = ""
        try:
            raw = response.choices[0].message.content.strip()
        except Exception:
            raw = str(response)

        # Try direct JSON parse first
        parsed = None
        try:
            parsed = json.loads(raw)
        except Exception:
            # Attempt to find a JSON substring in the LLM output
            m = re.search(r"\{[\s\S]*\}", raw)
            if m:
                try:
                    parsed = json.loads(m.group(0))
                except Exception:
                    parsed = None

        # If parsing succeeded and has expected keys, use it
        if isinstance(parsed, dict) and "event" in parsed and "choices" in parsed:
            event = str(parsed.get("event", "")).strip()
            choices = [str(c).strip() for c in parsed.get("choices", []) if str(c).strip()]
            # Ensure choices is a list of strings
            if not isinstance(choices, list):
                choices = []
            return {"event": event, "phase": parsed.get("phase", phase), "message": raw, "choices": choices}

        # Fallback: try to heuristically extract short choices from raw text
        # Look for numbered or dashed lists after the first line
        lines = [l.strip() for l in raw.splitlines() if l.strip()]
        event_short = lines[0] if lines else ""
        choices = []

        # search for lines starting with digits or dashes (1.  - )
        for l in lines[1:]:
            if re.match(r'^\d+\.\s+', l) or re.match(r'^[\-\•]\s+', l):
                # strip leading numbering/dash
                choice = re.sub(r'^\d+\.\s+|^[\-\•]\s+', '', l).strip()
                if choice:
                    choices.append(choice)
            else:
                # also accept short lines (<=6 words) as potential choices
                if 0 < len(l.split()) <= 8:
                    choices.append(l)

            if len(choices) >= 3:
                break

        return {"event": event_short, "phase": phase, "message": raw, "choices": choices}

    except Exception as e:
        return {
            "event": f"Error generating event: {e}",
            "phase": input.get("phase", "narration"),
            "message": f"❌ Exception in generate_event: {e}",
            "choices": []
        }
