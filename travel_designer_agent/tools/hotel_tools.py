from agents import function_tool

@function_tool
def suggest_hotels(destination:str , nights:int , budget:str) -> str:
    """
    Mock hotel data for a given destination, nights, and budget.
    """

    return (
        f"🏨 Hotels in {destination} for {nights} nights on a {budget} budget:\n"
        f"  1. BudgetInn – $50/night\n"
        f"  2. Comfort Suites – $80/night\n"
        f"  3. LuxuryStay – $150/night\n"
    )
