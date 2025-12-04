from pydantic import BaseModel

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    status: str
    result: str

