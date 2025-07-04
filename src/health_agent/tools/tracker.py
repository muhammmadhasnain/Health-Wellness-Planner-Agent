from agents import function_tool, RunContextWrapper
from context import UserSessionContext



@function_tool
async def ProgressTrackerTool(
    context: RunContextWrapper[UserSessionContext]
) -> str:
    """
    Schedules a weekly check-in reminder for the user.
    Logs the check-in into the user's progress history.
    """
    context.progress_logs.append({
        "week": "0",
        "status": "check-in scheduled"
    })
    return "Weekly check-in scheduled and logged in progress history."