"""
Num: #323. Number of Connected Components in an Undirected Graph
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
Problem:
    You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
    Return the number of connected components in the graph.
Constraints:
    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    There are no repeated edges.
Example 1:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2
Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
"""

import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        vis = [False] * n
        components = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = collections.deque()
            q.appendleft(node)
            vis[node] = True

            while q:
                for x in adj[q.pop()]:
                    if vis[x]:
                        continue
                    q.appendleft(x)
                    vis[x] = True

        for i in range(n):
            if not vis[i]:
                bfs(i)
                components += 1

        return components

