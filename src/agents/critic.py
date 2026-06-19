from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from src.config import settings
from src.logger import get_logger
from src.state import ResearchState

logger = get_logger(__name__)

llm = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY,
    temperature=0
)


def critic_agent(state: ResearchState) -> ResearchState:
    """
    Reviews research notes and identifies
    the single most important missing area.
    """

    try:
        state["agent_status"]["critic"] = "running"

        prompt = f"""
You are a senior research reviewer.

Review the research notes below.

Research Notes:
{state["research_notes"]}

Instructions:
1. Identify the SINGLE most important missing area.
2. Return a very short gap description.
3. If the research is already sufficient,
   return exactly:

NONE

Return only the answer.
"""

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        gap = response.content.strip()

        if not gap:
            gap = "NONE"

        state["missing_areas"] = gap

        state["agent_status"]["critic"] = "done"

        logger.info(
            f"Critic result: {gap}"
        )

        return state

    except Exception as e:
        logger.error(
            f"Critic Agent failed: {str(e)}"
        )

        state["error_log"].append(
            f"Critic Agent: {str(e)}"
        )

        state["missing_areas"] = "NONE"

        state["agent_status"]["critic"] = "error"

        return state
    
def route_after_critic(
    state: ResearchState
) -> str:
    """
    Determines whether to continue
    researching or move to writer.
    """

    gap = state["missing_areas"]

    if (
        gap.upper().strip() == "NONE"
        or len(gap.strip()) < 5
        or state["iteration_count"]
        >= state["max_iterations"]
    ):
        return "writer"

    return "research"