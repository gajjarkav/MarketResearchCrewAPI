import asyncio
from fastapi import FastAPI, HTTPException
from app.crew_runner import kickoff_crew
from app.schemas import ResearchRequest, ResearchResponse

app = FastAPI(
    title="Market Research Crew API"
)

@app.post('/research', response_model=ResearchResponse)
async def generate_report(request: ResearchRequest):
    """
    main endpoint
    :param request:
    :return: report
    """
    try:
        result = await asyncio.to_thread(kickoff_crew, request.topic)

        return ResearchResponse(
            status="success",
            result=result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/health')
def health_check():
    return {'status': 'healthy'}