from agents import Agent
from tools.event_tool import generate_event

def create_item_agent(model) -> Agent:
    return Agent(
        name="Item Agent",
        instructions=(
            "You are ItemAgent. You handle reward phases. "
            "Call generate_event('reward') to describe the treasure or item found, "
            "and present it to the player."
        ),
        model=model,
        tools=[generate_event]
    )

