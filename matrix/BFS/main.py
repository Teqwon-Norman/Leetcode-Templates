from collections import deque

def bfs(grid: list[list[int]], x: int, y: int):
    q = deque([(x, y)])
    visited = set([(x, y)])

    while q:
        x, y = q.popleft()
        
        for row, col in [(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if row > 0 or col > 0 or row <= len(grid) or col <= len(grid[0]) or (row, col) not in visited:
                visited.add((row, col))
                q.append((row, col))