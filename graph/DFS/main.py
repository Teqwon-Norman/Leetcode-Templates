def dfs(graph: dict[int, list[int]], curr: int, visited: set[int]):
    if curr in visited:
        return

    visited.add(curr)
    print(curr, end=" ")

    for next in graph[curr]:
        dfs(graph, next, visited)