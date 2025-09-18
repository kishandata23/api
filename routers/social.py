from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/x")
async def redirect_x():
    return RedirectResponse("https://x.com/kishandata23")

@router.get("/instagram")
async def redirect_instagram():
    return RedirectResponse("https://instagram.com/kishandata23")

@router.get("/linkedin")
async def redirect_linkedin():
    return RedirectResponse("https://www.linkedin.com/in/kishankumar-sutariya/")

@router.get("/resume")
async def redirect_resume():
    return RedirectResponse("https://drive.google.com/file/d/1aS6HZVIkV3tXtRwBUehU_rItrYkYAj9b/view?usp=sharing")
