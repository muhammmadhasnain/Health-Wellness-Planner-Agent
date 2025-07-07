from pydantic import BaseModel , Field
from typing import Optional


class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plain: Optional[dict] = None
    meal_plain: Optional[list[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: list[str] = Field(default_factory=list)
    progress_logs: list[dict[str, str]] = Field(default_factory=list)


    