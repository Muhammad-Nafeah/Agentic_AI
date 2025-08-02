from agents import Agent
from tools.event_tool import generate_event
from tools.dice_tool import roll_dice

def create_monster_agent(model) -> Agent:
    return Agent(
        name="Monster Agent",
        instructions=(
            "You are MonsterAgent. You handle combat phases. "
            "First, call generate_event('combat') to describe the enemy encounter. "
            "Then call roll_dice(sides, count) to resolve attack rolls, "
            "and narrate the results."
        ),
        model=model,
        tools=[generate_event, roll_dice]
    )