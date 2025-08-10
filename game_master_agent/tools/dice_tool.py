# dice_tool.py
import random
from agents import function_tool
from typing_extensions import TypedDict

class DiceInput(TypedDict):
    sides: int
    count: int

class DiceOutput(TypedDict):
    rolls: list[int]
    total: int
    message: str

@function_tool
async def roll_dice(input: DiceInput) -> DiceOutput:
    faces = input.get("sides", 6)
    count = input.get("count", 1)
    rolls = [random.randint(1, faces) for _ in range(count)]
    total = sum(rolls)
    message = f"🎲 You rolled: {rolls}  (Total = {total})"
    return {"rolls": rolls, "total": total, "message": message}