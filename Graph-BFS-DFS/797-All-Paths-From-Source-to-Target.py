"""
Num: #797. All Paths From Source to Target
Link: https://leetcode.com/problems/all-paths-from-source-to-target/
Problem: 
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
Constraints:
    * n == graph.length
    * 2 <= n <= 15
    * 0 <= graph[i][j] < n
    * graph[i][j] != i (i.e., there will be no self-loops).
    * All the elements of graph[i] are unique.
    * The input graph is guaranteed to be a DAG.
Example 1:
    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:
    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

# key point - after dfs(), path.pop()
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        target = n-1
        adj = [[] for i in range(n)]
        paths = []
        path = [0]
        
        for i, edge in enumerate(graph):
            adj[i].extend(edge)
        
        def dfs(i, path):
            if i == target:
                paths.append(list(path))
                return
            for k in adj[i]:
                path.append(k)
                dfs(k, path)
                path.pop()
            
        dfs(0, path)
        return paths
        
# Runtime: 125 ms, faster than 53.51% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.6 MB, less than 79.60% of Python3 online submissions for All Paths From Source to Target.     
            

# dfs - 
# reference: leetcode-solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            next_nodes = graph[node]
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()

        paths = []
        path = []
        if not graph or len(graph) == 0:
            return paths
        dfs(0)
        return paths

"""
Complexity Analysis
1. Time Complexity: O(2^V * V). Here, V represents the number of vertices.
- For a directed acyclic graph (DAG) with V vertices, there could be at most 2^{V - 1} - 1 possible paths to go from the starting vertex to the target vertex. 
  We need O(V) time to build each such path.
- Therefore, a loose upper bound on the time complexity would be (2^{V - 1} - 1) * O(V) = O(2^V * V).
- Since we have overlap between the paths, the actual time spent on the traversal will be lower to some extent.

2. Space Complexity: O(V). 
- The recursion depth can be no more than V, and we need O(V) space to store all the previously visited vertices while recursively traversing deeper with the current path. 

"""