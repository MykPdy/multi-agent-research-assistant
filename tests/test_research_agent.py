from src.state import initial_state
from src.agents.research import research_agent

state = initial_state(
    query="Future of AI Agents in Enterprises"
)

print("\nFIRST EXECUTION")
print("-" * 50)

state = research_agent(state)

first_length = len(state["research_notes"])

print(f"Research Notes Length: {first_length}")
print(f"Iteration Count: {state['iteration_count']}")
print(f"Sources Count: {len(state['sources'])}")

print("\nSECOND EXECUTION")
print("-" * 50)

state = research_agent(state)

second_length = len(state["research_notes"])

print(f"Research Notes Length: {second_length}")
print(f"Iteration Count: {state['iteration_count']}")
print(f"Sources Count: {len(state['sources'])}")

print("\nVERIFICATION")
print("-" * 50)

print(f"Notes Grew: {second_length > first_length}")
print(f"Iterations: {state['iteration_count']}")
print(f"Errors: {state['error_log']}")