from agents import function_tool, RunContextWrapper
from dataclasses import dataclass
from config import client

@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""

@function_tool
async def get_flights(wrapper: RunContextWrapper, input: UserTravelContext) -> str:
    """
    Get flights for specified destination
    """

    try :
        prompt = (
            f"Get flights for {input.destination} based on the user's mood: {input.mood}."
            "Do not hallucinate. If you dont know about any flights just create some random flights."
            "Format the output clearly as a list of flights."
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