def dfs(grid: list[list[int]], i: int, j: int, visited: set[list[int]]):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited:
        return
    
    visited.add((i, j))
    dfs(grid, i+1, j, visited)
    dfs(grid, i-1, j, visited)
    dfs(grid, i, j+1, visited)
    dfs(grid, i, j-1, visited)

