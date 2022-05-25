"""
Num: #547. Number of Provinces
Link: https://leetcode.com/problems/number-of-provinces/
Problem: 
    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
    A province is a group of directly or indirectly connected cities and no other cities outside of the group.
    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
    Return the total number of provinces.
Constraints:
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
Example 1:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2
Example 2:
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
"""

# key point - 'vis'
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        components = 0
        vis = [False] * n
        
        def dfs(i):
            if vis[i]:
                return
            
            vis[i] = True
            for j in range(n):
                if isConnected[i][j] == 1:
                    dfs(j)
            
        
        for i in range(n):
            if not vis[i]: 
                dfs(i)
                components += 1
        
        return components

# Runtime: 210 ms, faster than 78.08% of Python3 online submissions for Number of Provinces.
# Memory Usage: 14.9 MB, less than 12.26% of Python3 online submissions for Number of Provinces.