"""
Num: # 101. Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/
Problem: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true
Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false
Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(l, r):
            if not l and not r: return True
            if l and r and l.val == r.val:
                return isMirror(l.left, r.right) and isMirror(l.right, r.left)
            return False
        return isMirror(root, root)