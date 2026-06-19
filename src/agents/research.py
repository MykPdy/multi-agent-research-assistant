from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from src.config import settings
from src.logger import get_logger
from src.search import search_web
from src.state import ResearchState

logger = get_logger(__name__)

llm = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY,
    temperature=0
)


def research_agent(state: ResearchState) -> ResearchState:
    """
    Research agent:
    - Searches the web
    - Extracts research insights
    - Appends findings to research_notes
    - Deduplicates sources
    """

    try:
        state["agent_status"]["research"] = "running"

        query = state["query"]

        logger.info(
            f"Research iteration {state['iteration_count'] + 1}"
        )

        search_results = search_web(query)

        if not search_results:
            raise Exception(
                "No search results returned."
            )

        source_text = ""

        for idx, result in enumerate(
            search_results,
            start=1
        ):
            source_text += (
                f"\n[{idx}] {result['title']}\n"
                f"URL: {result['url']}\n"
                f"{result['content']}\n"
            )

        prompt = f"""
You are a research analyst.

Question:
{query}

Search Results:
{source_text}

Instructions:
1. Extract important facts.
2. Identify trends.
3. Identify opportunities.
4. Identify risks.
5. Use citation tags like [1], [2], [3].
6. Produce detailed research notes.
"""

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        new_notes = response.content

        if state["research_notes"]:
            state["research_notes"] += (
                "\n\n" + new_notes
            )
        else:
            state["research_notes"] = new_notes

        existing_sources = set(
            state["sources"]
        )

        for result in search_results:
            url = result["url"]

            if url and url not in existing_sources:
                state["sources"].append(url)
                existing_sources.add(url)

        state["iteration_count"] += 1

        state["agent_status"]["research"] = "done"

        logger.info(
            "Research completed successfully."
        )

        return state

    except Exception as e:
        logger.error(
            f"Research agent failed: {str(e)}"
        )

        state["error_log"].append(
            f"Research Agent: {str(e)}"
        )

        state["agent_status"]["research"] = "error"

        return state