from langgraph.graph import(
    StateGraph,
    START,
    END
)

from src.state import(
    ResearchState,
    initial_state
)

from src.cache import(
    get_cached_result,
    save_cached_result
)

from src.logger import get_logger

from src.state import ResearchState

from src.agents.research import research_agent
from src.agents.critic import (
    critic_agent,
    route_after_critic
)

from src.agents.writer import writer_agent
from src.agents.reviewer import reviewer_agent

logger = get_logger(__name__)

graph_builder = StateGraph(
    ResearchState
)

graph_builder.add_node(
    "research",
    research_agent
)

graph_builder.add_node(
    "critic",
    critic_agent
)

graph_builder.add_node(
    "writer",
    writer_agent
)

graph_builder.add_node(
    "reviewer",
    reviewer_agent
)

graph_builder.add_edge(
    START,
    "research"
)

graph_builder.add_edge(
    "research",
    "critic"
)

graph_builder.add_edge(
    "writer",
    "reviewer"
)

graph_builder.add_edge(
    "reviewer",
    END
)

graph_builder.add_conditional_edges(
    "critic",
    route_after_critic,
    {
        "research": "research",
        "writer": "writer"
    }
)

research_graph = graph_builder.compile()

def run_research(
    query: str,
    max_iterations: int = 2
) -> ResearchState:
    """
    Executes the complete LangGraph workflow.

    Flow:

    Research
        ↓
    Critic
        ↓
    Research (optional loop)
        ↓
    Writer
        ↓
    Reviewer
    """

    logger.info(
        f"Starting research workflow: {query}"
    )

    cached_result = get_cached_result(query)

    if cached_result:
        logger.info(
            "Returning cached result."
        )

        return cached_result

    state = initial_state(
        query=query,
        max_iterations=max_iterations
    )

    result = research_graph.invoke(
        state
    )

    save_cached_result(
        query,
        result
    )

    logger.info(
        "Research workflow completed."
    )

    return result