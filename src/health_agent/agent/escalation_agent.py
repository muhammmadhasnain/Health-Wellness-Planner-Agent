from agents import Agent
from context import UserSessionContext
from prompts.health_prompts import ENSCALATION_AGENT_INSTRUCTION
from utils.model_config import model


EscalationAgent = Agent[UserSessionContext](
    name= "Enscalation informtion agent",
    handoff_description="An agent that connects users with a real human expert or certified health coach for further assistance.",
    instructions= ENSCALATION_AGENT_INSTRUCTION,
    model=model
)