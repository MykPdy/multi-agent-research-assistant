from src.graph import run_research

result = run_research(
    query="Future of AI Agents in Enterprises",
    max_iterations=2
)

print("\n")
print("=" * 80)
print("FINAL REPORT")
print("=" * 80)

print(
    result["final_report"][:3000]
)

print("\n")
print("=" * 80)
print("ITERATIONS")
print("=" * 80)

print(
    result["iteration_count"]
)

print("\n")
print("=" * 80)
print("AGENT STATUS")
print("=" * 80)

print(
    result["agent_status"]
)

print("\n")
print("=" * 80)
print("ERROR LOG")
print("=" * 80)

print(
    result["error_log"]
)