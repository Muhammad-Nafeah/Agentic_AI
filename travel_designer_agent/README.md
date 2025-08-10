# 🌍 AI Travel Designer Agent

An *AI Chat-Based App* that empowers multi-agent to plans full travel experiences by coordinating between specialized agents:

- **DestinationAgent** – Recommends destinations based on mood or interests  
- **BookingAgent** – Simulates flight and hotel booking via `get_flights()` & `suggest_hotels()` tools  
- **ExploreAgent** – Suggests attractions, activities, and local food  

A top-level **TriageAgent** routes user queries to the right specialist, ensuring a seamless travel planning conversation.

---

## ⚙️ Features

1. **Destination Recommendation**  
   – “I’m in the mood for a relaxing beach getaway.”  
   – Returns 2–3 curated destinations.

2. **Mock Booking**  
   – “Book me a flight from New York to Bali on 2025-09-01:2025-09-10.”  
   – Uses `get_flights()` and then `suggest_hotels()` based on user’s dates, nights, and budget.

3. **Local Exploration**  
   – “What should I do in Phuket?”  
   – Lists top attractions and local dining tips.

4. **Graceful Fallbacks**  
   – Handles ambiguous or unsupported requests with polite clarification prompts.

---

## 🛠️ Tech Stack & Dependencies

- **Python 3.10+**  
- [OpenAI Agent SDK](https://github.com/openai/openai-python)  
- **Tools**  
  - `agents.tools.function_tool` decorator  
- **Environment**  
  - `python-dotenv` for loading `.env` (Gemini API key)  

---

## 🚀 Getting Started

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/ai_travel_designer.git
   cd ai_travel_designer

2. **Create & activate a virtual environment (optional but recommended)**
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

3. **Install dependencies**
    pip install -r requirements.txt

4. **Configure your Gemini API key**
    GEMINI_API_KEY=ya29.YOUR_ACTUAL_KEY_HERE

5. **Run the CLI**
    python run main.py

## 💬 Sample Interaction
👋 AI Travel Designer Agent — type 'exit' to quit.

You: I’m in the mood for a relaxing beach getaway.

💡 DestinationAgent: How about these destinations?
  1. Bali – beautiful beaches & rice terraces
  2. Phuket – clear waters & night markets
  3. Maldives – overwater bungalows & snorkeling

You: Phuket

💡 BookingAgent: 
✈️ Flight from JFK to HKT on 2025-09-01:2025-09-10:
  • Airline: MockAir
  • Price: $650 round-trip

🏨 Hotels in Phuket for 5 nights on a medium budget:
  1. BudgetInn – $50/night
  2. Comfort Suites – $80/night
  3. LuxuryStay – $150/night

You: What should I do there?

💡 ExploreAgent:
  1. Patong Beach – water sports & nightlife
  2. Big Buddha – scenic landmark
  3. Old Town – street food & local markets

You: exit

👋 Goodbye!


## 🙋 Author
Syed Muhammad Nafeah
BSCS – 3rd Semester, Sir Syed University of Engineering & Technology
GitHub: Muhammad-Nafeah


