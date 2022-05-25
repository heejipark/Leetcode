"""
Num: #200 Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Problem: 
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'
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


# DFS - 1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numIsland = 0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == '0':
                return 0
            
            grid[i][j] = '0'  
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i+x, j+y)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    numIsland += 1
                    
        return numIsland 

# Runtime: 302 ms, faster than 91.40% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.4 MB, less than 80.37% of Python3 online submissions for Number of Islands.


# BFS - 1
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        numIsland = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                
                q.appendleft((i,j))
                grid[i][j] = '0'
                numIsland += 1
                
                while q:
                    x, y = q.pop()
                    for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = x+r, y+c
                        
                        if nr<0 or nc<0 or nr>=m or nc>=n or grid[nr][nc] == '0':
                            continue
                        
                        q.append((nr,nc))
                        grid[nr][nc] = '0'
                
        return numIsland

# Runtime: 720 ms, faster than 5.01% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.2 MB, less than 90.92% of Python3 online submissions for Number of Islands.