"""
Num: #144. Binary Tree Preorder Traversal
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem: Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [1]
    Output: [1]
"""

# Approach 1: Iterations
# Start from the root and then at each iteration opo the current node out of the stack and push its child nodes.
# In the implemented strategy we push nodes into output list following the order Top->Bottom and Left->Right, that naturally reproduces preorder taversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        stack, output = [root], []
        
        # Preorder: root-left-right => Therefore, append root.right first. Stack is FILO.
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
                    
        return output
    
# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.
# Space complexity : depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).
# Runtime: 26 ms, faster than 97.26% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.9 MB, less than 58.24% of Python3 online submissions for Binary Tree Preorder Traversal.