from agents import Agent
from dataclasses import dataclass
from config import model

@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""

explore_agent = Agent[UserTravelContext](
        name="ExploreAgent",
        instructions="Recommend top attractions, foods, and experiences for the destination in context.",
        model=model,
    )