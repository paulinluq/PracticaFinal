from pydantic import BaseModel

class Feedback(BaseModel):
    pagina: str
    calificacion: int
    feedback: str