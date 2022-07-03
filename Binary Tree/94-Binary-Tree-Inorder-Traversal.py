"""
Num: #94. Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Problem: Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [1]
    Output: [1]
"""

# 1. Recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: left-root-right
        def inorder(root,res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
        
        res=[]
        inorder(root,res)
        return res
                
# Runtime: 55 ms, faster than 18.92% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.8 MB, less than 58.80% of Python3 online submissions for Binary Tree Inorder Traversal.


# 2. Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result, stack = [], []
        
        # "while True" block keeps running until "return"
        while True:

            # travel to each node's left child, till reach the left leaf
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return result
            
            node = stack.pop() # The node has no left child
            result.append(node.val) # so let's append the node value 
            root = node.right # Visit its right child --> if it has left child ? append left and left.val
                              # Otherwise append node.val, then visit right child again... root = node.right

