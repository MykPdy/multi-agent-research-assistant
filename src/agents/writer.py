from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from src.config import settings
from src.logger import get_logger
from src.state import ResearchState

logger = get_logger(__name__)

llm = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY,
    temperature=0.2,
    max_tokens=4000
)

def writer_agent(state: ResearchState) -> ResearchState:
    """
    Converts research notes into
    a structured research report.
    """

    try:
        state["agent_status"]["writer"] = "running"
        sources_text = "\n".join(state["sources"])
        prompt = f"""
You are a professional research report writer.

Using ONLY the research notes below,
create a detailed report.

Research Notes:

{state["research_notes"]}

Sources:

{sources_text}

IMPORTANT RULES:

1. Use ONLY information from the research notes.
2. Do NOT add new information.
3. Do NOT invent citations.
4. Every factual claim should include citations such as [1], [2], [3].
5. You MUST include every section below.
6. Never omit a section.
7. If information is limited, write the section anyway and explicitly state the limitation.

OUTPUT FORMAT:

# Executive Summary

(write content)

# Key Findings

(write content)

# Detailed Analysis

(write content)

# Comparison and Trade-offs

(write content)

# Challenges and Limitations

(write content)

# Conclusion

(write content)

# Sources

(list all provided source URLs)

Return valid Markdown.
"""

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        report = response.content
        # DEBUGGING
        print("\n" + "=" * 80)
        print("REPORT LENGTH")
        print("=" * 80)
        print(len(report))

        print("\n" + "=" * 80)
        print("LAST 500 CHARACTERS")
        print("=" * 80)
        print(report[-500:])

        required_sections = [
            "# Executive Summary",
            "# Key Findings",
            "# Detailed Analysis",
            "# Comparison and Trade-offs",
            "# Challenges and Limitations",
            "# Conclusion",
            "# Sources"
        ]

        missing_sections = [
            section
            for section in required_sections
            if section not in report
        ]
        if missing_sections:
            logger.warning(
                f"Writer output missing sections: {missing_sections}"
            )

            state["error_log"].append(
                f"Writer validation warning: Missing sections {missing_sections}"
            )
        state["draft_report"] = report

        state["agent_status"]["writer"] = "done"

        logger.info(
            "Writer Agent completed successfully."
        )

        return state

    except Exception as e:
        logger.error(
            f"Writer Agent failed: {str(e)}"
        )

        state["error_log"].append(
            f"Writer Agent: {str(e)}"
        )

        state["agent_status"]["writer"] = "error"

        return state