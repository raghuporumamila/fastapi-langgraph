from fastapi import APIRouter
from app.schemas.email import EmailRequest, EmailResponse
from app.agents.email_agent import build_email_graph

router = APIRouter()
email_graph = build_email_graph()

@router.post("/generate-email", response_model=EmailResponse)
def generate_email(request: EmailRequest):
    state = {
        "intent": request.intent,
        "tone": request.tone,
        "context": request.context,
        "email": ""
    }

    result = email_graph.invoke(state)
    return {"email": result["email"]}
