"""
Num: #1971 Find if Path Exists in Graph
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Problem: 
    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
    You want to determine if there is a valid path that exists from vertex source to vertex destination.
    Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
Constraints:
    * 1 <= n <= 2 * 105
    * 0 <= edges.length <= 2 * 105
    * edges[i].length == 2
    * 0 <= ui, vi <= n - 1
    * ui != vi
    * 0 <= source, destination <= n - 1
    * There are no duplicate edges.
    * There are no self edges.
Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2
Example 2:
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.
"""

import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        adj = [[] for i in range(n)]
        vis = set()
        
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        q = collections.deque([source])
        
        while q:
            for k in adj[q.pop()]:
                if k == destination: return True
                if k in vis: continue
                vis.add(k)
                q.appendleft(k)
        return False
        
# Runtime: 2129 ms, faster than 75.13% of Python3 online submissions for Find if Path Exists in Graph.
# Memory Usage: 102 MB, less than 98.96% of Python3 online submissions for Find if Path Exists in Graph.        
     

import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        # set the edges
        graph = collections.defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        
        # check if edge was visited or not
        visited = set()
        q = collections.deque([source])
        
        while q:
            n = q.pop()
            visited.add(n)
            for edge in graph[n]:
                if edge == destination:
                    return True
                if edge not in visited:
                    visited.add(edge)
                    q.appendleft(edge)
                    
        return False
                    
# Runtime: 1725 ms, faster than 98.25% of Python3 online submissions for Find if Path Exists in Graph.
# Memory Usage: 106.4 MB, less than 56.59% of Python3 online submissions for Find if Path Exists in Graph.