"""
Num: #145. Binary Tree Postorder Traversal
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem: Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:
    Input: root = [1,null,2,3]
    Output: [3,2,1]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [1]
    Output: [1]
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Postorder: left-right-root
        def postorder(root,res):
            if root:
                postorder(root.left, res)
                postorder(root.right, res)
                
                res.append(root.val)
        
        res=[]
        inorder(root,res)
        return res