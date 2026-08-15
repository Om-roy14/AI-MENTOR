from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from services.log_service import save_log
from services.prompt_service import build_prompt
from services.ai_service import generate_roadmap
from services.email_service import send_email


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@router.post("/generate-roadmap", response_class=HTMLResponse)
async def generate(

    request: Request,

    name: str = Form(...),

    email: str = Form(...),

    skill: str = Form(...),

    goal: str = Form(...),

    experience: str = Form(...),

    daily_time: str = Form(...),

    learning_style: str = Form(...),

    notes: str = Form("")

):

    # =========================
    # BUILD PROMPT
    # =========================

    prompt = build_prompt(

        name,
        skill,
        goal,
        experience,
        daily_time,
        learning_style,
        notes

    )


    # =========================
    # GENERATE ROADMAP
    # =========================

    roadmap = generate_roadmap(prompt)


    # =========================
    # SEND EMAIL
    # =========================

    try:

        send_email(
            receiver=email,
            name=name,
            roadmap=roadmap
        )

        # Save log locally if database is enabled.
        # Automatically skipped on Vercel.
        save_log(
            name=name,
            email=email,
            skill=skill,
            status="SUCCESS"
        )

    except Exception as e:

        save_log(
            name=name,
            email=email,
            skill=skill,
            status="FAILED",
            error=str(e)
        )

        raise e


    # =========================
    # SUCCESS PAGE
    # =========================

    return templates.TemplateResponse(

        request=request,

        name="success.html",

        context={

            "request": request,

            "name": name

        }

    )