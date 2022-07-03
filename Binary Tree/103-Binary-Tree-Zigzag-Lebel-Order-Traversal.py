"""
Num: #103. Binary Tree Zigzag Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Problem: 
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]
Example 2:
    Input: root = [1]
    Output: [[1]]
Example 3:
    Input: root = []
    Output: []
Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. BFS
import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # BFS - queue
        # queue - root. 
        # level -> for len(queue)
        # pop []
        
        q = collections.deque([root]) # queue = FIFO
        level = 0
        result = []
        if not root:
            return root
        while q:
            level += 1
            levels = []
            for _ in range(len(q)):
                node = q.popleft()
                levels.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if level % 2 != 0: # odd
                result.append(levels) 
            else: # even
                result.append(levels[::-1])
        
        return result


# 2. Recursive 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        
        if root is None:
            return []
        
        def levelOrder(root, level):
            if level == len(levels):
                levels.append([])
            
            if level % 2 == 0:
                levels[level].append(root.val)
            else:
                levels[level].insert(0,root.val) # for zigzag shape
            
            
            if root.left:
                levelOrder(root.left, level+1)
            if root.right:
                levelOrder(root.right, level+1)
                
        
        levelOrder(root,0)
        
        return levels
            