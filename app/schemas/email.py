from pydantic import BaseModel

class EmailRequest(BaseModel):
    intent: str
    tone: str
    context: str

class EmailResponse(BaseModel):
    email: str
