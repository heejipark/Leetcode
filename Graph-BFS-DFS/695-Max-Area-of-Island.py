"""
Num: #695 Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/
Problem: 
    Return the maximum area of an island in grid. If there is no island, return 0.
Example 1:
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
Explanation:
    The answer is not 11, because the island must be connected 4-directionally.
Solution:
    1. check the all grid whether the area is equal to 1 or 0
    2. If the area is equal to 1: add by 1 for counting the the number of area
                                and move on to neighbor areas (4-dirctionally)
    3. else: ignore the area and move on to next area
    4. Using DFS, BFS
"""


# BFS - 1
import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                size = 0
                grid[i][j] = 0
                q = collections.deque()
                q.appendleft((i,j))
                
                
                while q:
                    x, y = q.pop()
                    size += 1
                    
                    for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r+x, c+y
                        if nr<0 or nc<0 or nr>=m or nc>=n or grid[nr][nc]==0:
                            continue
                        
                        q.appendleft((nr,nc))
                        grid[nr][nc] = 0
                        
                    maxArea = max(maxArea, size)
        
        return maxArea

# DFS - 1
# main keypoint: store the visited area as a set() type.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # initialize the variables
        m, n = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or (i,j) in visited:
                return 0
            
            visited.add((i,j))
            
            return (1 + 
                    dfs(i+1,j) +
                    dfs(i-1, j) +
                    dfs(i,j+1) +
                    dfs(i, j-1))
            
        
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea, dfs(i,j))
        
        return maxArea

# DFS - 2
# main keypoint: change the visited area as a '0' and store the size of area with a nonlocal variable.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        size = 0
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            
            nonlocal size
            size += 1
            grid[i][j] = 0
            
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = i+x
                nc = j+y
                dfs(nr,nc)
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = 0
                    dfs(i,j)
                    maxArea = max(maxArea, size)
        
        return maxArea





# reference: @dpjungmin, @neetcode