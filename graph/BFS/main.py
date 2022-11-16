from collections import deque

def bfs(graph: dict[int, list[int]], node: int):
    q = deque([node])
    visited = set([node])

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        for next in graph[curr]:
            if next in visited:
                continue

            q.append(next)
            visited.add(next)
