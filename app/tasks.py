from crewai import Task
from app.prompts import researcher, analyst, editor, writer

class MarketResearchTasks:
    def research_task(self, agent, topic):
        return Task(
            description=researcher.task(topic=topic),
            expected_output=researcher.expected_output(),
            agent=agent
        )

    def analysis_task(self, agent):
        return Task(
            description=analyst.task(),
            expected_output=analyst.expected_output(),
            agent=agent
        )

    def writing_task(self, agent):
        return Task(
            description=writer.task(),
            expected_output=writer.expected_output(),
            agent=agent
        )

    def editing_task(self, agent):
        return Task(
            description=editor.task(),
            expected_output=editor.expected_output(),
            agent=agent,
            output_file="final_article.md"
        )