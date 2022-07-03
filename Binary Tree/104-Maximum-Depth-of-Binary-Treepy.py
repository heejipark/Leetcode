"""
Num: #104. Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Problem: 
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
Example 2:
    Input: root = [1,null,2]
    Output: 2
Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iteration 2 - BFS using queue  (Tips: BFS-queue / DFS-stack)
import collections
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        depth = 0
        q = collections.deque([root])

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
        return depth

# Runtime: 67 ms, faster than 31.84% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.3 MB, less than 89.77% of Python3 online submissions for Maximum Depth of Binary Tree.



# Iteration 2 - DFS using stack
class Solution:
    def maxDepth(self, root):
        stack = []
        if root:
            stack.append((1, root))
        
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth

# Time complexity : O(N).
# Space complexity : 
# in the worst case, the tree is completely unbalanced, O(n) : e.g. each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). 
# But in the average case (the tree is balanced), the height of the tree would be log(N). 
# Therefore, the space complexity in this case would be O(log(N)).


# Recursive 1- Top-down
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1

# Time complexity : we visit each node exactly once, thus the time complexity is O(N), where NN is the number of nodes.
# Space complexity : 
# in the worst case, the tree is completely unbalanced, O(n) : e.g. each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). 
# But in the average case (the tree is balanced), the height of the tree would be log(N). 
# Therefore, the space complexity in this case would be O(log(N)).


# Recursive 2- Bottom up
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def findDepth(root,depth,answer):
            if not root:
                return
            if not root.left or not root.right:
                answer = max(answer, depth)
            findDepth(root.left, depth+1, answer)
            findDepth(root.right, depth+1, answer)
        
        maxdepth = findDepth(root,1,answer)
        return maxdepth
        

