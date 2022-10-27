from collections import deque


dirs = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs(grid: list[list[int]], _i: int, _j: int):
    q = deque([[_i, _j]])
    visited = set([(_i, _j)])

    while q:
        curr = q.popleft()
        for dir in dirs:
            i = curr[0] + dir[0]
            j = curr[1] + dir[1]

            if i < 0 or j > 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited:
                continue

            visited.add((i, j))
            q.append([i, j])