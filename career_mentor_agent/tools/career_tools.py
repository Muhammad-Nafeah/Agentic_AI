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

class CareerRoadmapInput(TypedDict):
    career_field: str


@function_tool
async def get_career_roadmap(wrapper: RunContextWrapper, input: CareerRoadmapInput) -> dict:
    """
    Generate a step-by-step learning roadmap for a given career field.
    Expects input = {"career_field": "<field name>"}
    Returns {"skill_roadmap": "<bullet or numbered list>"} or {"error": "<message>"}
    """

    try:
        print("🚀 Invoking get_career_roadmap tool with input:", input)
        
        prompt = (
        f"I'm interested in becoming a {input['career_field']}.\n"
        "Please provide a clear, step-by-step skill roadmap divided into beginner, intermediate, and advanced stages.\n"
        "Format your answer using bullet points or numbered steps."
        )

        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response.choices[0].message.content.strip()
        return {"skill_roadmap": output.strip()}

    except Exception as e:
        print("❌ Exception in get_career_roadmap tool:", str(e))
        return {
            "error": f"❌ Exception in get_career_roadmap tool: {str(e)}"
        }
