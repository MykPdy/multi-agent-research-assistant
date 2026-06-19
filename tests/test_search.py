from src.search import search_web


results = search_web(
    "Latest developments in AI agents"
)

print()

for idx, result in enumerate(results, start=1):
    print(f"[{idx}] {result['title']}")
    print(result["url"])
    print()