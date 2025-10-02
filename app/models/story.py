
from pydantic import BaseModel, Field
from typing import List, Optional


class Story(BaseModel):
    title: str = Field(..., min_length=3)
    description: str
    acceptance_criteria: List[str]

class RequirementRequest(BaseModel):
    requirement_text: str
    project: Optional[str] = None

class StoryResponse(BaseModel):
    stories: List[Story]