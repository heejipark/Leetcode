"""
Num: #543. Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Problem: 
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.
Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
    Input: root = [1,2]
    Output: 1
Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. DFS
"""
Key obeservation to make is: 
1. 'the longest path has to be between two leaf nodes.'
2. Find the node where the sum of its longest left and right branches is maximized.
- Because nodes are only connected with their parent node and 2 children, so we found out that the longest path in the tree would consist of a node, its longest left branch and its longest right branch.
3. Apply DFS to count each node's branch lengths, because it would allow us to dive deep into the leaves first, and then start counting the edges upwards.

Caution:
In the midst of DFS, we also need to take the following two cases into account
    1) The current node's both left and right branches might be a part of the longest path.
    2) One fo the current node's left of right branches might be a part of the longest path.

So, We are going to address them by
    1) applying DFS to recursively find the longest branches starting the node's left and right children.
    2) Initializing a global variable diameter to keep track of the longest path and updating it at each node with the sum of the node's left and right branches.
    3) returning the length of the longest branch between a node's left and right brances.

Algorithm:
    1) Initialize an integer varialbe 'dimeter' to keep track of the longest path we find from the DFS.
    2) Implement a recursive function 'longestPath' which takes a TreeNode as input. It should recursively explore the entire tree rooted at the given node. Once it's finished, it should return the longest path out of its left and right branches:
        - If 'node' is 'None', we have reached the end of the tree, hence we should return 0;
        - We want to recursively exlore node's children, so we call longestPath again with node's left and right children. In return, we get the longest path of its left and right children 'leftPath' and 'rightPath'
        - If 'leftPath' plus 'rightPath' is longer than the current longest diameter found, then we nee to update 'diameter'
        - Finally, we return the longer one of 'leftPath' and 'rightPath'. 
        - Remember to add 1 as the edge connecting it with its parent.
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        
        def longest(node):
            if not node: return 0
            nonlocal diameter
            
            # recursively find the longest path in
            # both left child and right child
            left_path = longest(node.left)
            right_path = longest(node.right)
            
            # update the diameter if left_path and right_path is larger
            diameter = max(diameter, left_path + right_path)
            
            # return the longest one between left_path and right_path
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1
        
        longest(root)
        return diameter
    
# Let N be the number of nodes in the tree
# Time complexity: O(N) This is because in our recursion function longestPath, we only enter and exit from each node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.
# Spance complexity: O(N) The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(logN).
        


