from agents import function_tool, RunContextWrapper
from context import UserSessionContext
from datetime import datetime


@function_tool
async def checkinSchedulerTool(
    context: RunContextWrapper[UserSessionContext]
    ) -> str:
    today = datetime.today().strftime("%Y-%m-%d")
    context.progress_log.append({
        "date": today,
        "status": "check-in scheduled"
    })

    return f"Check-in scheduled for today: {today} and logged in progress."