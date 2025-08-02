from agents import function_tool
import random

@function_tool
def roll_dice(sides: int=6 , count: int=1) -> str:
    """
    Roll `count` fair dice with `sides` sides and return the individual and total results.
    """
    rolls = [random.randint(1,sides) for _ in range(count)]
    total = sum(rolls)
    rolls_str = ", ".join(str(r) for r in rolls)
    return f"🎲 You rolled: [{rolls_str}]  (Total = {total})"

    




