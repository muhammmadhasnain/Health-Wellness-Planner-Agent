from pydantic import BaseModel 
from typing import Optional , List


class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plain: Optional[dict] = None
    meal_plain: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[dict[str, str]] = []


    