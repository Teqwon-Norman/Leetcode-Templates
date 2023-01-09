from collections import deque

"""
Most matrix problems require you to find a range of consistent values
such as the famous problems involving islands, this is a great template
"""

def solve(grid: list[list[int]]):
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                bfs(grid, r, c)

def bfs(grid: list[list[int]], x: int, y: int):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for row, col in [(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if inbounds(grid, row, col) or (row, col) == 1:
                q.append((row, col))

def inbounds(grid, r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        return True
    return False