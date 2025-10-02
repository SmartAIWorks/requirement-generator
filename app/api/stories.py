
from fastapi import APIRouter, HTTPException

from app.models.story import RequirementRequest
from app.services.llm_service import generate_stories

router = APIRouter(prefix="/stories", tags=["stories"])

@router.post("/generate")
async def generate(req: RequirementRequest):

    try:
        stories = generate_stories(req.requirement_text)
        return {"stories": stories}
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))