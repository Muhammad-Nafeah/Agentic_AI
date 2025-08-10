from agents import RunContextWrapper, function_tool
from typing import List
from config import client
from dataclasses import dataclass

@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""
@function_tool
async def suggest_hotels(wrapper: RunContextWrapper, input: UserTravelContext) -> List[str]:
    """
    Suggest hotels for specified destination
    """

    try:
        prompt = (
            f"Suggest hotels for {input.destination} based on the user's mood: {input.mood}."
            "Do not hallucinate. If you dont know about any hotels just create some random hotels."
            "Format the output clearly as a list of hotels."
        )
        response = await client.chat.completions.create(
            model = "gemini-2.0-flash",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
