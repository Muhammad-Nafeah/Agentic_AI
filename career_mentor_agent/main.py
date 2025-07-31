import os 
import sys
from dotenv import load_dotenv

from agents import AsyncOpenAI , OpenAIChatCompletionsModel , Runner 
from agents.run import RunConfig

from agent.main_agent import create_main_agent


def main() -> None:

    # loading .env and checking the key
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: Gemini API Key is not set in .env", file = sys.stderr)
        sys.exit(1) #program ends due to an error or abnormal condition
    
    #client
    client = AsyncOpenAI(
        api_key = api_key,
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    #wrapping client into chat completion model
    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash",
        openai_client = client
    )
    #configuring runner
    config = RunConfig(
        model = model,
        tracing_disabled = True,
    )

    # triage_agent = create_main_agent(model)
    triage_agent, agent_map = create_main_agent(model)

    print("👋 Welcome to Career Mentor Agent!  Type 'exit' to quit.\n")

    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ("exit", "quit"):
                print("👋 Goodbye! See you soon.")
                break

            result = Runner.run_sync(
                starting_agent=triage_agent,
                input=user_input,
                run_config=config
                )

            if result.final_output.startswith("HANDOFF: "):
                agent_name = result.final_output.split("HANDOFF: ", 1)[1].strip()
                if agent_name in agent_map:
                    specialist_agent = agent_map[agent_name]
                    specialist_result = Runner.run_sync(
                        starting_agent=specialist_agent,
                        input=user_input,
                        run_config=config
                    )
                    print(f"\n💡 Mentor ({specialist_agent.name}): {specialist_result.final_output}\n")
                else:
                    print(f"\n💡 Mentor: Error: Unknown agent '{agent_name}'\n")

            else:
                print(f"\n💡 Mentor ({triage_agent.name}): {result.final_output}\n")

    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye! 👋")



if __name__ == "__main__":
    main()





