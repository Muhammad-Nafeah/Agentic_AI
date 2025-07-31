#job_agent
from agents import Agent

def create_job_agent(model) -> Agent:
    return Agent(
        name = "Job Agent",
        instructions = (
            "You are JobAgent. "
            "For a given career field, list 3 real‑world job roles "
            "and for each give a one‑sentence description."
            ),
        model = model
    )
