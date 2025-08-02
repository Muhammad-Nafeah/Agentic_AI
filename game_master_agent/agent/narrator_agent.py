from agents import Agent

def create_narrator_agent(model) -> Agent:
    return Agent(
        name="Narrator Agent",
        instructions=(
            "You are NarratorAgent. You open and advance the adventure story. "
            "At each turn, generate a short scene description by calling the event tool "
            "if needed, then prompt the player for their next action."
        ),
        model=model
    )