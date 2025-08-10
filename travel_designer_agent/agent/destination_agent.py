from agents import Agent
from dataclasses import dataclass
from config import model 

@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""

destination_agent = Agent[UserTravelContext](
        name="DestinationAgent",
        instructions=
        """You are DestinationAgent.
        Ask the user about their mood or interests and suggest a matching travel destination. Always store the destination in context.""",
        model=model,
    )