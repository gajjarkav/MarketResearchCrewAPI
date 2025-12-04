import requests as rq
from crewai.tools import BaseTool
from config import settings

class NewsTool(BaseTool):
    name: str = "News Search"
    description: str = (
        "Useful for searching the latest headlines and news articles on a specific topic."
        "Use this when you need current events or breaking news. "
        "Input should be a search topic (e.g., 'Quantum Computing')."
    )
    def _run(self, topic: str) -> str:
        """
        fetch news articles using news.org apikey
        :param topic:
        :return: news articles
        """

        if not settings.NEWS_API_KEY:
            raise ValueError("NEWS_API_KEY must be set")

        url = "https://newsapi.org/v2/everything"

        payload = {
            'q': topic,
            'language': 'en',
            'sortBy': 'relevancy',
            'pageSize': 5,
            'apiKey': settings.NEWS_API
        }

        try:
            response = rq.get(url=url, params=payload)
            response.raise_for_status()
            data = response.json()

            articles = data.get('articles', [])

            if not articles:
                return f"no news found for topic {topic}"

            results = []

            for article in articles:
                title = article.get('title', 'no title')
                source = article.get('source', {}).get('name', 'unknown source')
                description = article.get('description', 'no description')
                url = article.get('url', '#')

                results.append(f"- **{title}** ({source}): {description} [Link]({url})")
            return "\n".join(results)

        except Exception as e:
            return f"error fetching news : {str(e)}"