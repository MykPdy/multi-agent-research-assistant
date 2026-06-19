from typing import TypedDict, List, Dict


class ResearchState(TypedDict):
    query: str

    research_notes: str

    sources: List[str]

    missing_areas: str

    draft_report: str

    final_report: str

    iteration_count: int

    max_iterations: int

    error_log: List[str]

    agent_status: Dict[str, str]


def initial_state(
    query: str,
    max_iterations: int = 2
) -> ResearchState:
    return {
        "query": query,
        "research_notes": "",
        "sources": [],
        "missing_areas": "",
        "draft_report": "",
        "final_report": "",
        "iteration_count": 0,
        "max_iterations": max_iterations,
        "error_log": [],
        "agent_status": {
            "research": "pending",
            "critic": "pending",
            "writer": "pending",
            "reviewer": "pending"
        }
    }