from src.state import initial_state
from src.agents.research import research_agent

state = initial_state(
    query="Future of AI Agents in Enterprises"
)

updated_state = research_agent(state)

print("\n")
print("=" * 80)
print("RESEARCH NOTES")
print("=" * 80)

print(
    updated_state["research_notes"]
)

print("\n")
print("=" * 80)
print("SOURCES")
print("=" * 80)

for source in updated_state["sources"]:
    print(source)