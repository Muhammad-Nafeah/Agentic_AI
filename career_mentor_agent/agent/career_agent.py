#career_agent
from agents import Agent

def create_career_agent(model) -> Agent:
    return Agent(
        name = "Career Agent",
        instructions=(
            "You are CareerAgent. "
            "Based on the student's interests, suggest 3 suitable career fields "
            "formatted as a numbered list."
            ),
        model = model
        )
