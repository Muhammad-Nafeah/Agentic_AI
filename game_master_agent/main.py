# main.py
import chainlit as cl
from agents import Runner
from agent.main_agent import game_master_agent
from config import model, config

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    cl.user_session.set("agent", game_master_agent)
    await cl.Message("🗺️ Welcome, adventurer! Your quest begins now.").send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history", [])
    game_master_agent = cl.user_session.get("agent")

    history.append({"role": "user", "content": msg.content})
    cl.user_session.set("last_action", msg.content)

    thinking = cl.Message("⚔️ Adventuring...")
    await thinking.send()

    try:
        result = await Runner.run(
            game_master_agent,
            history,
            run_config=config
        )
        output = result.final_output

        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()