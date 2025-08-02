from agents import function_tool

@function_tool
def get_flights(origin:str , destination:str , date:str) -> str:
    """
    Mock flight data for a given origin, destination, and travel dates.
    """
    return (
        f"✈️ Flight from {origin} to {destination} on {date}:\n"
        f"  • Airline: MockAir\n"
        f"  • Price: $650 round-trip\n"
    )
