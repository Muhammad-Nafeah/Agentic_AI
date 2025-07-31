import os,sys

from dotenv import load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Runner
from agents.run import RunConfig

from agent.main_agent import main_agent

def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY missing in .env", file=sys.stderr)
        sys.exit(1)

    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
    )

    config = RunConfig(
        model=model,
        tracing_disabled=True
    )

    triage_agent , agent_map = main_agent(model)

    print("👋 AI Travel Designer Agent — type 'exit' to quit.\n")

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