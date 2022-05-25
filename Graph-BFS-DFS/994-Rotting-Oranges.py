"""
Num: #994 Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/
Problem: 
    You are given an m x n grid where each cell can have one of three values:
    * 0 representing an empty cell,
    * 1 representing a fresh orange, or
    * 2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

# BFS - 1
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        minute = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: fresh += 1                
                if grid[i][j] == 2: q.appendleft((i,j))
        
        while q:
            qsize = len(q)
            for _ in range(qsize):
                x, y = q.pop()  # rotten orange
                for r, c in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = x+r, y+c
                    if nr>=0 and nc>=0 and nr<m and nc<n and grid[nr][nc] == 1:
                        q.appendleft((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            # if q is empty, we have to prevent adding the minute.
            print(q, minute)
            if q: 
                minute += 1
    
        if fresh: 
            return -1    
        
        return minute