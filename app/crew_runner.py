from crewai import Crew, Process
from app.agents import MarketResearchAgent
from app.tasks import MarketResearchTasks

# --> for api use
def kickoff_crew(topic: str) -> str:
    agents = MarketResearchAgent()
    tasks = MarketResearchTasks()

    researchAgent = agents.senior_research_agent()
    analystAgent = agents.market_analyst_agent()
    writerAgent = agents.content_writer_agent()
    editorAgent = agents.senior_editor_agent()

    task1 = tasks.research_task(researchAgent, topic)
    task2 = tasks.analysis_task(analystAgent)
    task3 = tasks.writing_task(writerAgent)
    task4 = tasks.editing_task(editorAgent)

    crew = Crew(
        agents=[researchAgent, analystAgent, writerAgent, editorAgent],
        tasks=[task1, task2, task3, task4],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return str(result)

# --> for cli use
"""agents = MarketResearchAgent()
tasks = MarketResearchTasks()

TOPIC = "AI Agents in 2025"

researchAgent = agents.senior_research_agent()
analystAgent = agents.market_analyst_agent()
writerAgent = agents.content_writer_agent()
editorAgent = agents.senior_editor_agent()

task1 = tasks.research_task(researchAgent, TOPIC)
task2 = tasks.analysis_task(analystAgent)
task3 = tasks.writing_task(writerAgent)
task4 = tasks.editing_task(editorAgent)

crew = Crew(
    agents=[researchAgent, analystAgent, writerAgent, editorAgent],
    tasks=[task1, task2, task3, task4],
    process=Process.sequential,
    verbose=True
)

print(f"## Starting crew for {TOPIC} ##")

result = crew.kickoff()

print("-"*25,"result","-"*25)
print(result)"""