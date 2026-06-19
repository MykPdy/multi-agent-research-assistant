from src.state import initial_state
from src.agents.research import research_agent
from src.agents.writer import writer_agent

state = initial_state(
    query="Future of AI Agents in Enterprises"
)

state = research_agent(state)

state = writer_agent(state)

print("\n")
print("=" * 80)
print("DRAFT REPORT")
print("=" * 80)

print(state["draft_report"][:3000])

print("\n")
print("=" * 80)
print("REPORT LENGTH")
print("=" * 80)

print(len(state["draft_report"]))