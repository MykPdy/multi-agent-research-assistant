from src.state import initial_state
from src.agents.research import research_agent
from src.agents.critic import (
    critic_agent,
    route_after_critic
)

state = initial_state(
    query="Future of AI Agents in Enterprises"
)

state = research_agent(state)

state = critic_agent(state)

print("\n")
print("=" * 80)
print("CRITIC RESULT")
print("=" * 80)

print(state["missing_areas"])

print("\n")
print("=" * 80)
print("ROUTE")
print("=" * 80)

print(
    route_after_critic(state)
)