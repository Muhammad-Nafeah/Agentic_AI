# config.py

import os 
from agents import AsyncOpenAI , OpenAIChatCompletionsModel 
from dotenv import load_dotenv, find_dotenv
from agents.run import RunConfig    

#loading env variable
load_dotenv(find_dotenv())

api_key = os.getenv("GEMINI_API_KEY")
# Check API key
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")

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
    model_provider=client,
    tracing_disabled = True,
)