from src.state import initial_state

from src.agents.research import research_agent
from src.agents.critic import critic_agent
from src.agents.writer import writer_agent
from src.agents.reviewer import reviewer_agent

state = initial_state(
    query="Future of AI Agents in Enterprises"
)

state = research_agent(state)

state = critic_agent(state)

state = writer_agent(state)

state = reviewer_agent(state)

print("\n")
print("=" * 80)
print("FINAL REPORT")
print("=" * 80)

print(state["final_report"][:3000])

print("\n")
print("=" * 80)
print("FINAL REPORT LENGTH")
print("=" * 80)

print(len(state["final_report"]))

print("\n")
print("=" * 80)
print("AGENT STATUS")
print("=" * 80)

print(state["agent_status"])

print("\n")
print("=" * 80)
print("ERROR LOG")
print("=" * 80)

print(state["error_log"])