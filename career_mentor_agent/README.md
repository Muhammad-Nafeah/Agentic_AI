# 💼 Career Mentor Agent

A terminal-based AI project that helps students explore career paths using a multi-agent system powered by the **OpenAI Agent SDK**.

---

## 🌟 What It Does

This intelligent assistant guides users through their career journey by:

- 🎯 **Recommending Career Paths** based on user interests
- 🛠️ **Showing Skill Roadmaps** using a built-in `get_career_roadmap()` tool
- 🔄 **Handoff Between Agents** to provide specialized advice:
  - `CareerAgent` – suggests possible fields
  - `SkillAgent` – provides learning plans and required skills
  - `JobAgent` – shares real-world job titles and roles

---

## ⚙️ How It Works

- 🔁 **OpenAI Agent SDK + Runner**: Manages conversation flow and agent switching
- 🧰 **Tool Support**: A custom skill roadmap tool enhances the advice
- 🤖 **Multi-Agent System**: Routes queries to the most suitable agent using handoff logic

---

## 🧠 Agents Used

| Agent        | Role                                |
|--------------|-------------------------------------|
| CareerAgent  | Detects user's field of interest    |
| SkillAgent   | Returns skills needed for that path |
| JobAgent     | Shares job roles and career options |

---

## 🛠️ Tech Stack

- Python 3
- OpenAI `agentflow` SDK
- Terminal-based interaction (no UI)
- Modular folder structure for agents/tools

---

## 📁 Folder Structure

career_mentor_agents/
├── agents/
│ ├── agent.py # Base Agent class
│ ├── career_agent.py # Handles field suggestions
│ ├── skill_agent.py # Provides skill learning plan
│ └── job_agent.py # Shares job roles
├── tools/
│ └── career_tools.py # get_career_roadmap() function
├── main.py # Entry point, runs chat loop
├── requirements.txt
└── README.md

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/your-username/career_mentor_agents.git
cd career_mentor_agents

pip install -r requirements.txt

uv run main.py


💬 Sample Interaction
You: I want to become a mobile app developer.

💡 Mentor (CareerAgent): Sounds great! You're interested in Mobile Development.
HANDOFF: SkillAgent

💡 Mentor (SkillAgent): To become a Mobile App Developer:
1. Learn Java or Kotlin (Android) / Swift (iOS)
2. Study UI/UX principles
3. Explore Android Studio or Xcode
...

🙋‍♂️ Author
Syed Muhammad Abdul Nafeah
BSCS – 4th Semester
Sir Syed University of Engineering & Technology
Part of IT Course at Governor House, Karachi
GitHub: Muhammad-Nafeah
