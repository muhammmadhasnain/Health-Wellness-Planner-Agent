from agents import Agent
from context import UserSessionContext
from prompts.health_prompts import NUTRITION_EXPERT_AGENT_INSTRUCTION
from utils.model_config import model


NutritionExpertAgent = Agent[UserSessionContext](
    name= "Nutrition Agent",
    handoff_description="An agent that provides personalized nutritional guidance and meal plans for users with complex dietary needs like diabetes or allergies.",
    instructions= NUTRITION_EXPERT_AGENT_INSTRUCTION,
    model=model
    

)