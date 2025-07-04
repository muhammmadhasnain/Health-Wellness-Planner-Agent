from agents import function_tool, RunContextWrapper
from context import UserSessionContext
import re


@function_tool
async def GoalAnalyzerTool(
    context: RunContextWrapper[UserSessionContext],
    user_input

) -> str :
    """
    This tool converts the user's goal into a structured format.
    Example: "I want to lose 5kg in 2 months"
    Output: {"goal_type": "weight_loss", "amount": "5kg", "duration": "2 months"}
    """


    text = user_input.lower()

    if "lose" in text:
        goal_type = "weight_lose"
    elif "gain" in text:
        goal_type = "weight_gain"
    else: 
        goal_type = "fitness"

    
    match = re.search(r"(\d+)\s?(kg|pounds)? .* in (\d+)\s?(weeks|months|mahine)", text)

    if match:
        amount = match.group(1) + (match.group(2) or "")
        duration = match.group(3) + " " + match.group(4)
        

        structured_goal = {
            "goal_type": goal_type,
            "amount": amount,
            "duration": duration
        }

        context.goal = structured_goal
        
        return f"Goal extracted successfully: {structured_goal}"
    else:
        return "Sorry, I couldn’t understand your goal. Please try again with more details."