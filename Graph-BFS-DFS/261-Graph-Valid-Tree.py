"""
Num: #261. Graph Valid Tree
Link: https://leetcode.com/problems/graph-valid-tree/
Problem: 
    You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
    Return true if the edges of the given graph make up a valid tree, and false otherwise.
Constraints:
    1 <= n <= 2000
    0 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no self-loops or repeated edges.
Example 1:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true
Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false
"""
"""
What is Tree? -> G, is a tree iff the following two conditions are met:
1. G contains no cycles. Check whether or not there are n - 1 edges. If there's not, then return false.
   - For the graph to be a valid tree, it must have exactly n - 1 edges. 
   - Any less, and it can't possibly be fully connected. 
   - Any more, and it has to contain cycles. 
2. Check whether or not the graph is fully connected. Return true if it is, false if otherwise.
-> To sum up, if the graph is fully connected and contains exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!

Depth-first search is a classic graph-traversal algorithm that can be used to check for both of these conditions:
- G is fully connected if, and only if, we started a depth-first search from a single source and discovered all nodes in G during it.
- G contains no cycles if, and only if, the depth-first search never goes back to an already discovered node. 
  We need to be careful though not to count trivial cycles of the form A → B → A that occur with most implementations of undirected edges.
"""

# DFS - 1
# Key point - (1) len(edges) == n (2) sum(vis) == n
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1: return False
        adj = [[] for i in range(n)]
        vis = [False] * n
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i):
            if vis[i]: return
            vis[i] = True
            
            for k in adj[i]:
                if vis[k]: continue    
                dfs(k)
        
        dfs(0)
        return sum(vis) == n
# Runtime: 99 ms, faster than 84.36% of Python3 online submissions for Graph Valid Tree.
# Memory Usage: 16.1 MB, less than 35.65% of Python3 online submissions for Graph Valid Tree.



# BFS - 1
# Key point - (1) len(edges) == n (2) sum(vis) == n
import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # The condition of Tree
        if len(edges) != n-1: return False
        
        adj = [[] for i in range(n)]
        vis = [False] * n
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def bfs(i):
            q = collections.deque()
            q.appendleft(i)
            vis[i] = True
            
            while q:
                for k in adj[q.pop()]:
                    if vis[k]: continue
                    q.appendleft(k)
                    vis[k] = True
                    
        bfs(0)
        return sum(vis) == n
# Runtime: 105 ms, faster than 72.43% of Python3 online submissions for Graph Valid Tree.
# Memory Usage: 15.4 MB, less than 71.46% of Python3 online submissions for Graph Valid Tree.
        