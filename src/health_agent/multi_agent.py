import asyncio
from agents import Agent, Runner
from context import UserSessionContext
from prompts.health_prompts import HEALTH_WELNESS_AGENT_INSTRUCTIONS
from agent.escalation_agent import EscalationAgent
from agent.injury_support_agent import InjurySupportAgent
from agent.nutrition_expert_agent import NutritionExpertAgent
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import checkinSchedulerTool
from tools.tracker import ProgressTrackerTool
from utils.model_config import model, config
from guardrails import health_input_guardrail, health_output_guardrail
from guardrails import MessageOutput





health_wellness_agent = Agent[UserSessionContext](
    name="Health Wellness Agent",
    handoff_description="An agent that helps users create personalized health and fitness plans based on their goals, diet preferences, and physical conditions.",
    instructions=HEALTH_WELNESS_AGENT_INSTRUCTIONS,
    tools=[
        GoalAnalyzerTool,
        MealPlannerTool,
        WorkoutRecommenderTool,
        checkinSchedulerTool,
        ProgressTrackerTool

    ],
    
    handoffs=[
        EscalationAgent, 
        InjurySupportAgent,
        NutritionExpertAgent
    ],

    input_guardrails=[
        health_input_guardrail
    ],

    output_guardrails=[
        health_output_guardrail
    ], 
    output_type=MessageOutput,
    model=model

)

