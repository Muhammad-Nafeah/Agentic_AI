from agents import Agent
from dataclasses import dataclass
from config import model
from tools.flight_tools import get_flights, suggest_hotels

@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""

booking_agent = Agent[UserTravelContext](
        name="BookingAgent",
        instructions=
        """You are BookingAgent.
        Use get_flights and suggest_hotels tools to simulate booking a trip for the selected destination. Show flights and hotels.""",
        model=model,
        tools=[get_flights, suggest_hotels],
    )

