from agents import function_tool, RunContextWrapper
from context import UserSessionContext



@function_tool
async def MealPlannerTool(
    context: RunContextWrapper[UserSessionContext],
    ) -> list[str]:

    """
    Suggests a 7-day meal plan based on user's dietary preferences and goal.
    """

    diet = context.diet_preferences or "general"
    goal = context.goal.get() if context.goal else "fitness"

    meals = {
         "vegetarian": ["Oats", "Vegetable Curry", "Lentil Soup"],
        "diabetic": ["Boiled Eggs", "Grilled Chicken Salad", "Quinoa Bowl"],
        "keto": ["Avocado Omelet", "Zucchini Noodles", "Steak & Veggies"],
        "general": ["Toast & Eggs", "Chicken Wrap", "Rice & Beans"]
    }

    selected_meals = meals.get(diet , meals["general"])

    plan = []

    for day in range(1, 8):
        meal = (
            f"Day {day}: Breakfast: {selected_meals[0]}, "
            f"Lunch: {selected_meals[1]}, Dinner: {selected_meals[2]} "
            f"({diet} diet, Goal: {goal})"
        )

        plan.append(meal)

    context.meal_plain = plan
    return plan