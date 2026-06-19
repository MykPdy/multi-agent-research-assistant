from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from src.config import settings
from src.logger import get_logger
from src.state import ResearchState

logger = get_logger(__name__)

llm = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY,
    temperature=0.1
)


def reviewer_agent(state: ResearchState) -> ResearchState:
    """
    Polishes the report without adding
    new information.
    """

    try:
        state["agent_status"]["reviewer"] = "running"

        prompt = f"""
You are a senior editor.

Review the report below.

Rules:

1. Do NOT add new information.
2. Do NOT remove citations.
3. Improve grammar.
4. Improve readability.
5. Improve structure and formatting.
6. Keep all sections.

Report:

{state["draft_report"]}

Return the improved report.
"""

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        state["final_report"] = response.content

        state["agent_status"]["reviewer"] = "done"

        logger.info(
            "Reviewer Agent completed successfully."
        )

        return state

    except Exception as e:
        logger.error(
            f"Reviewer Agent failed: {str(e)}"
        )

        state["error_log"].append(
            f"Reviewer Agent: {str(e)}"
        )

        state["final_report"] = (
            state["draft_report"]
        )

        state["agent_status"]["reviewer"] = "error"

        return state