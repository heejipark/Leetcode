"""
Num: # 133. Clone Graph
Link: https://leetcode.com/problems/clone-graph/
Problem: 
    Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
Test case format:
    For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
    An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
    The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        vis = {}
        
        q = collections.deque([node])
        vis[node] = Node(node.val, [])
        
        while q:
            x = q.pop()
            for neighbor in x.neighbors:
                if neighbor not in vis:
                    vis[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                vis[x].neighbors.append(vis[neighbor])
        

        return vis[node]

# Runtime: 41 ms, faster than 81.83% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.4 MB, less than 77.92% of Python3 online submissions for Clone Graph.

"""
Complexity Analysis
1. Time Complexity : O(N + M), where N is a number of nodes (vertices) and M is a number of edges.
2. Space Complexity : O(N). This space is occupied by the visited dictionary and in addition to that, space would also be occupied by the queue since we are adopting the BFS approach here. The space occupied by the queue would be equal to O(W) where W is the width of the graph. Overall, the space complexity would be O(N).
"""