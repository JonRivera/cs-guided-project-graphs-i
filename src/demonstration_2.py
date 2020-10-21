"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
"""DEPTH FIRST SEARCH ALGO SOL"""
from collections import deque


# def numIslands(grid):
#     # Your code here
# Function Annotation Representation
def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = ''
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)

    ans = 0
    if not grid or not grid[0]:
        return ans

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                ans += 1
                dfs(grid, i, j)

    return ans
