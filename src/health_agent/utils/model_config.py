import os
from dotenv import load_dotenv, find_dotenv
from agents import  AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEM_API_KEY")

# Async client for external model (Gemini-style API)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model configuration
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Run configuration

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)