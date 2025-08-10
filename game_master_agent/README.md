# 🎲 Game Master Agent (Fantasy Adventure CLI)

A terminal-based, multi-agent fantasy adventure game built with the OpenAI Agent SDK. Players progress through an interactive story, enter combat, and collect rewards—all orchestrated by specialized AI agents.

---

## 🌟 What It Does

- **NarratorAgent**: Sets the scene and advances the story  
- **MonsterAgent**: Handles combat encounters, uses `generate_event("combat")` and `roll_dice()`  
- **ItemAgent**: Manages rewards and inventory, uses `generate_event("reward")`  
- **GameMasterAgent (Triage)**: Routes player input to the appropriate specialist agent  

---

## 🛠️ Tech Stack & Dependencies

- **Python 3.10+**  
- **OpenAI Agent SDK** (`openai-agents`)  
- **python-dotenv** for environment variable management  
- **Random** (built-in) for dice rolls and event selection  

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/Agentic_AI.git
   cd Agentic_AI/game_master_agent

2. **Create & activate a virtual environment (optional)**
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

3. **Install dependencies**

    pip install -r requirements.txt

4. **Configure your API key**
    
    Configure your API key

5. **Run the game**

    python main.py or uv run main.py


**💬 Sample Playthrough**

🎮 Game Master Agent — type 'exit' to quit.

You: Start the adventure.

💡 NarratorAgent: The salt spray stings your face as the "Sea Serpent" crests another wave...
What do you do?

You: I look around the deck.

💡 NarratorAgent: You spot a loose plank and a locked chest at your feet...

You: Attack the guard crab.

💡 MonsterAgent: A giant crab snaps its pincers at you!
🎲 You rolled: [4, 2] (Total = 6)

You: Open the chest.

💡 ItemAgent: You find a chest of gold coins and a healing potion.

You: Exit

👋 Thanks for playing!

**🙋 Author**
Syed Muhammad Nafeah
4th Semester, BS Computer Science
Sir Syed University of Engineering & Technology
GitHub: Muhammad-Nafeah

