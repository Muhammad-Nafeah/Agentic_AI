from agents import function_tool
import random

@function_tool
def generate_event(phase: str) -> str:
    """
    Generate a random game event description for the given phase:
    'narration', 'combat', or 'reward'.
    """
    events = {
        "narration": [
            "You enter a dark cave and hear distant dripping water.",
            "A friendly villager warns you of bandits ahead.",
            "The forest path opens onto a misty lake at dawn."
        ],
        "combat": [
            "A goblin leaps at you with a rusty dagger!",
            "A giant spider descends from above, fangs dripping venom!",
            "An undead warrior blocks your path, sword raised."
        ],
        "reward": [
            "You find a chest of gold coins and a healing potion.",
            "A mysterious merchant gifts you a magical ring.",
            "You discover an ancient scroll of fireball."
        ]
    }

    choices = events.get(phase, [])
    if not choices:
        return f"No events available for phase '{phase}'."
    return random.choice(choices)
