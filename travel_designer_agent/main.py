import chainlit as cl
from agents import Agent, Runner
from agents.run import RunConfig
from dataclasses import dataclass
from typing import cast
from agent.main_agent import triage_agent
from config import config


@dataclass
class UserTravelContext:
    user_id: str
    mood: str = ""
    destination: str = ""

@cl.on_chat_start
async def start():
    cl.user_session.set("agent", triage_agent)
    cl.user_session.set("config", config)
    cl.user_session.set("chat_history", [])
    cl.user_session.set("user_context", UserTravelContext(user_id="Ahmed"))

    await cl.Message(content="Welcome to the AI Travel Designer! Where would you like to go today?").send()

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Planning your travel experience...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))
    history = cl.user_session.get("chat_history") or []
    context: UserTravelContext = cast(UserTravelContext, cl.user_session.get("user_context"))

    history.append({"role": "user", "content": message.content})

    try:
        result = await Runner.run(
            starting_agent=agent,
            input=history,
            context=context,
            run_config=config,
        )

        response_content = result.final_output

        msg.content = response_content
        await msg.update()

        history.append({"role": "developer", "content": response_content})
        cl.user_session.set("chat_history", history)

        print(f"History: {history}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")