"""
Num: #102. Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Problem:
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level). 
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
Example 2:
    Input: root = [1]
    Output: [[1]]
Example 3:
    Input: root = []
    Output: []
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approach 1: Recursion
- Ensure that the tree is not empty. Call recursive the function helper(node, level), which takes the current node and its level as the arguments
1. The output list here is called levels, and hence the current level is just a length of this list len(levels) Compare the numver of a current level len(levels)
 with a node level 'level'. If you're still on the previous level - add the new one by adding a new list into levels.
2. Append the node value to the last list in 'levels'
3. Process recursively child nodes if they are not None: helper(node.left/node.right, level+1) 
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
        levels = []
        if not root: 
            return levels
        
        def helper(node, level):
            # Start the current level
            if len(levels) == level:
                levels.append([])
            
            # Append the current node value
            levels[level].append(node.val)
            
            # Process child nodes for the next level
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
            
        helper(root, 0)
        return levels

# Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(N) to keep the output structure which contains N node values.
# Runtime: 79 ms, faster than 5.50% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 15 MB, less than 8.89% of Python3 online submissions for Binary Tree Level Order Traversal.
        

"""
Approach2: Iteration using Queue(FIFO)
Let's keep nodes of each tree level in the queue structure, which typically orders elements in a FIFO.

1. Initiate queue with a root and start from the level number 0: level = 0
2. While queue is not empty:
    - Start the current level by adding an emplty list into output structure levels.
    - Compute how many elements should be on the current level: it's a queue length.
    - Pop out all these elements from the queue and add them into the current level
    - Push their cild nodes into the queue for the next level.
    - Go to the next level level+=1.

"""
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            # go to next level
            level += 1
        
        return levels
# Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(N) to keep the output structure which contains N node values.
# Runtime: 54 ms, faster than 37.46% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.3 MB, less than 25.91% of Python3 online submissions for Binary Tree Level Order Traversal.
            
