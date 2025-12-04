from crewai import Agent, LLM
from crewai_tools import SerperDevTool

from config import settings
from app.prompts import researcher, analyst, writer, editor

llm = LLM(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_API_BASE,
    model=f"groq/{settings.MODEL_NAME}"
)
search_tool = SerperDevTool(api_key=settings.SERPER_API_KEY)

class MarketResearchAgent:

    def senior_research_agent(self):
        return Agent(
            role=researcher.role(),
            goal=researcher.goal(),
            backstory=researcher.backstory(),
            tools=[search_tool],
            allow_delegation=False,
            llm=llm,
            verbose=True,
            memory=True
        )

    def market_analyst_agent(self):
        return Agent(
            role=analyst.role(),
            goal=analyst.goal(),
            backstory=analyst.backstory(),
            allow_delegation=False,
            llm=llm,
            verbose=True,
        )

    def content_writer_agent(self):
        return Agent(
            role=writer.role(),
            goal=writer.goal(),
            backstory=writer.backstory(),
            allow_delegation=False,
            llm=llm,
            verbose=True,
        )

    def senior_editor_agent(self):
        return Agent(
            role=editor.role(),
            goal=editor.goal(),
            backstory=editor.backstory(),
            allow_delegation=False,
            llm=llm,
            verbose=True,
        )