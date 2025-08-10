from agents import Agent,handoff
from agent.booking_agent import booking_agent
from agent.explore_agent import explore_agent
from agent.destination_agent import destination_agent
from utils.orchestrator import orchestrator_handoff
from dataclasses import dataclass
from config import model 

@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""


triage_agent = Agent[UserTravelContext](
        name="Triage Agent",
        instructions="""You are a helpful TriageAgent.
        Use DestinationAgent to suggest destinations based on mood, BookingAgent to book flights and hotels, and ExploreAgent to suggest attractions and food.""",
        model=model,
        handoffs=[
            handoff(agent=destination_agent, on_handoff=orchestrator_handoff(destination_agent)),
            handoff(agent=booking_agent, on_handoff=orchestrator_handoff(booking_agent)),
            handoff(agent=explore_agent, on_handoff=orchestrator_handoff(explore_agent))
        ]
    )
