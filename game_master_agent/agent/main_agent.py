from agents import Agent
from agent.item_agent import create_item_agent
from agent.monster_agent import create_monster_agent
from agent.narrator_agent import create_narrator_agent


def create_main_agent(model):

    narrator_agent=create_narrator_agent(model)
    item_agent=create_item_agent(model)
    monster_agent=create_monster_agent(model)

    triage_agent=Agent(
        name="Triage Agent",
        instructions=(
            "You are GameMasterAgent. Based on the player's input or the story phase, "
            "decide which specialist agent to invoke next:\n"
            "- For advancing the story and setting scenes, hand off to NarratorAgent.\n"
            "- For resolving fights or encounters, hand off to MonsterAgent.\n"
            "- For distributing loot or describing rewards, hand off to ItemAgent.\n"
            "Respond with exactly `HANDOFF: <AgentName>` and no other text."
        ),
        model=model,
        handoffs=[narrator_agent, item_agent, monster_agent]
    )
    agent_map={
        "NarratorAgent": narrator_agent,
        "ItemAgent": item_agent,
        "MonsterAgent": monster_agent,
    }

    return triage_agent, agent_map