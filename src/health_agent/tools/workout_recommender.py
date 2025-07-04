from agents import function_tool, RunContextWrapper
from context import UserSessionContext


@function_tool
async def WorkoutRecommenderTool(
    context: RunContextWrapper[UserSessionContext]
    ) -> str:
    """
    Suggests a basic weekly workout plan based on user's goal.
    """

    goal = context.goal or {}

    workout_plan = []

    if "weight_lose" in goal.get("goal_type", ""):
        workout_plan = [
            "Monday: Cardio - 30 minutes running",
            "Tuesday: Full Body Strength",
            "Wednesday: Cycling",
            "Thursday: Yoga or Stretching",
            "Friday: Weight Lifting",
            "Saturday: Outdoor Walk",
            "Sunday: Rest"
        ]
    else: 
        workout_plan = [
            "Monday: Strength Training",
            "Tuesday: Light Walk",
            "Wednesday: HIIT",
            "Thursday: Yoga",
            "Friday: Cardio",
            "Saturday: Mixed Weights",
            "Sunday: Rest"
        ]

    context.workout_plain = {"weekly_plain": workout_plan}

    return "Here's your workout plan:\n" +  "\n".join(workout_plan)