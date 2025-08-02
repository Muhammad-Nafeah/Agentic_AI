from agents import Agent

from agent.explore_agent import create_explore_agent
from agent.destination_agent import create_destination_agent
from agent.booking_agent import create_booking_agent

def main_agent(model):

    booking_agent = create_booking_agent(model)
    explore_agent = create_explore_agent(model)
    destination_agent = create_destination_agent(model)

    triage_agent =Agent(
        name="Triage Agent",
        instructions="""
        You are Triage Agent. Read the user’s request and decide exactly which specialist should handle it:

        - If the user wants to **book travel** (flights or hotels), hand off to BookingAgent.
        - If the user asks **what to see or do** at a destination, hand off to ExploreAgent.
        - If the user asks **where to go** (e.g. “suggest a destination” or “I want a beach vacation”), hand off to DestinationAgent.

        Respond with exactly:
        HANDOFF: <AgentName>
        and nothing else. For example:
        HANDOFF: BookingAgent
        """,
        model=model,
        handoffs=[booking_agent, explore_agent, destination_agent]
    )
    agent_map={
        "BookingAgent": booking_agent,
        "ExploreAgent": explore_agent,
        "DestinationAgent": destination_agent
    }

    return triage_agent, agent_map