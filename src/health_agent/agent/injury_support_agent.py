from agents import Agent 
from context import UserSessionContext
from prompts.health_prompts import INGURY_SUPPORT_AGENT_INSTRUCTION
from utils.model_config import model



InjurySupportAgent = Agent[UserSessionContext](
    name = "Injury support agent",
    handoff_description="An agent that assists users with injury-specific workout and health advice, focusing on safe and recovery-friendly routines.",
    instructions = INGURY_SUPPORT_AGENT_INSTRUCTION,
    model=model
)