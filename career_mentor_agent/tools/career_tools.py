# career_tools
from agents import function_tool

@function_tool
def get_career_roadmap(input_field:str) -> str:
    """
    Return a career roadmap as bullet points for a given field.
    """

    roadmap_library = {
        "Data Science": {
            "Python basics": "2 weeks",
            "Statistics fundamentals": "3 weeks",
            "Machine Learning": "4 weeks",
            "Portfolio projects": "ongoing",
        },
        "Web Development": {
            "HTML & CSS": "1 week",
            "JavaScript": "2 weeks",
            "React": "3 weeks",
            "Backend (Node/Python)": "3 weeks",
        },
        "Product Management": {
            "Market research": "2 weeks",
            "Roadmapping": "2 weeks",
            "Agile basics": "2 weeks",
            "Stakeholder communication": "ongoing",
        },
    }

    skills = roadmap_library.get(input_field)
    if not skills:
        return f"Sorry! I dont have a roadmap for the field: {input_field}."
    
    result = "\n".join([f". {skill} -> {duration}" for skill,duration in skills.items()])
    return result



