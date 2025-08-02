# main_agent.py
from agents import Agent
from agent.career_agent import create_career_agent
from agent.job_agent import create_job_agent
from agent.skill_agent import create_skill_agent

def create_main_agent(model):
    career_agent = create_career_agent(model)
    job_agent = create_job_agent(model)
    skill_agent = create_skill_agent(model)
    
    triage_agent = Agent(
        name="Triage Agent",
        instructions=(
            "You are the Triage Agent. Read the user's request and decide which "
            "specialist agent to invoke:\n"
            "- If they ask about career suggestions, hand off to CareerAgent.\n"
            "- If they ask for a learning plan, hand off to SkillAgent.\n"
            "- If they ask about real-world roles, hand off to JobAgent.\n"
            "Respond with exactly `HANDOFF: <AgentName>` when handing off."
        ),
        model=model,
        handoffs=[career_agent, job_agent, skill_agent]
    )
    
    agent_map = {
        "CareerAgent": career_agent,
        "JobAgent": job_agent,
        "SkillAgent": skill_agent
    }
    
    return triage_agent, agent_map
