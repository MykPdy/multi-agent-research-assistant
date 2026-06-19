from typing import List, Dict

from tavily import TavilyClient
from duckduckgo_search import DDGS

from src.config import settings
from src.logger import get_logger

logger = get_logger(__name__)

tavily_client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


def search_tavily(
    query: str,
    max_results: int = 5
) -> List[Dict]:
    """
    Search using Tavily.
    """

    response = tavily_client.search(
        query=query,
        max_results=max_results
    )

    results = []

    for item in response.get("results", []):
        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "content": item.get("content", "")
            }
        )

    return results


def search_duckduckgo(
    query: str,
    max_results: int = 5
) -> List[Dict]:
    """
    Fallback search using DuckDuckGo.
    """

    results = []

    with DDGS() as ddgs:
        search_results = list(
            ddgs.text(
                query,
                max_results=max_results
            )
        )

    for item in search_results:
        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("href", ""),
                "content": item.get("body", "")
            }
        )

    return results


def search_web(
    query: str,
    max_results: int = 5
) -> List[Dict]:
    """
    Primary Tavily search with DDG fallback.
    """

    try:
        logger.info(
            f"Searching Tavily: {query}"
        )

        return search_tavily(
            query=query,
            max_results=max_results
        )

    except Exception as e:
        logger.error(
            f"Tavily failed: {str(e)}"
        )

        try:
            logger.info(
                f"Using DuckDuckGo fallback: {query}"
            )

            return search_duckduckgo(
                query=query,
                max_results=max_results
            )

        except Exception as ddg_error:
            logger.error(
                f"DuckDuckGo failed: {str(ddg_error)}"
            )

            return []