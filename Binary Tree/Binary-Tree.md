### Binary Tree

#### Good problems: 102, 104, 543, 101

#### What is tree?
: Each node of the tree will have a root value and a list of references to other nodes which are called child nodes.
From graph view, a tree can also be defined as a directed acyclic graph which has <b> N nodes </b> and <b> N-1 edges</b>.


#### What is binary tree?
: A Binary Tree is one of the most typical tree structure. As the name suggests, a binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

#### Traverse A Tree
- Be able to solve preorder, inorder and postorder traversal <b> recursively</b>;
- Be able to solve preorder, inorder and postorder traversal <b> iteratively</b>;
- Be able to do <b>level traversal</b> using <b>BFS</b>.

1) Pre-order Traversal (root-left-right)
: Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

2) In-order Traversal (left-root-right)
: In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.
Typically, for binary search tree, we can retrieve all the data in sorted order using in-order traversal.

3) Post-order Traversal (left-right-rooot)
: Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root. 

It is worth noting that when you delete nodes in a tree, deletion process will be in post-order. That is to say, when you delete a node, you will delete its left child and its right child before you delete the node itself.

Also, post-order is widely use in mathematical expression. It is easier to write a program to parse a post-order expression. If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.



### 1. Recursive Solution
##### Pre-order Traversal: Root-Left-Right
```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Postorder: root-left-right
        def preorder(root,res):
            if root:
                res.append(root.val) # visit the root
                preorder(root.left, res) # traverse left subtree
                preorder(root.right, res) # traverse right subtree
                
        res=[]
        preorder(root,res)
        return res
```

##### In-order Traversal: Left-Root-Right
```python
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
```

##### Post-order Traversal: Left-Right-Root
```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Postorder: left-right-root
        def postorder(root,res):
            if root:
                postorder(root.left, res)
                postorder(root.right, res)
                res.append(root.val)
        
        res=[]
        postorder(root,res)
        return res
```

##### Time complexity
The time complexity is O(N) because we visit each node exactly once. And the depth of the tree might be N in the worst case. That is to say, the level of recursion might be at most N in the worst case. 



#### Level-order Traversal
Level-order traversal is to traverse the tree level by level.
Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph. The algorithm starts with a root node and visit the node itself first. Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth.
Typically, we use a queue to help us to do BFS. 


#### Solve the Tree problem recursively

##### 1. "Top-down" Solution
"Top-down" means that in each recursive call, we well visit the node first to come up with some values, and pass these values to its children when calling the function recursively. 
So, the "top-down" solution can be considered as a kind of <b>preorder(root-left-right)</b> traversal. To be specific, the recursive function top_down(root, params) works like this:
```python
1. return specific value for null node
2. update the answer if needed
3. left_ans = top_down(root.left, left_params)
4. right_ans = top_down(root.right, right_params)
5. return the answer if needed
```

<br><br>
<b>maximum depth</b>
For instance, consider this problem: <i>Given a binary tree, find it maximum depth</i>

Here we will define the depth of the root node as 1 (although often, the dept of the root node is defined as 0). For each node, if we know its depth, we will know the depth of its children. Therefore, if we pass the depth of the node as a parameter when calling the function recursively, all the nodes will know their depth. And for leaf nodes, we can use the depth to update the final answer. Here is the pseudocode for the recursive function maximum_depth(root, depth)
```python
1. return if root is null
2. if root is a leaf node:
3.      answer = max(answer, depth) # undate the anser if needed
4. maximum_depth(root.left, depth+1) # call the function recursively for left child
5. maximum_depth(root.right, depth+1) # call the function recursively for right child
```

##### 2. "Bottom-up" Solution
In each recursive call, we'll firstly call the function recursively for all the children nodes and then come up with the answer according to the returned values and the vaue of the current node itself. This process can be regarded as a kind of postorder traversal. Typically, a "buttom-up" recursive function bottom_up(root) will be something like this:

```python
1. return specific value for null node
2. left_ans = bottom_up(root.left)      # call function recursively for left child
3. right_ans = bottom_up(root.right)    # call function recursively for right child
4. return answers                       # answer <-- left_ans, right_ans, root.val
```


<b>maximum depth</b>
If we know maximum depth <B>l</B> of the subtree rotted as its <B>left child</B> and the maximum depth <B>r</B> of the subtree rooted at its <B>right child</B>. We can choose the maximum between them and add 1 to get the maximum depth of the subtree rotted at the current node. That is <B>x = max(l,r) + 1</B>

It means that for each node, we can get the answer after solving the problem for its children. Therefore, we can solve this problem using a bottom-up solution. Here is the psedocode for therecursive function maximum_depth(root):

```python
1. return 0 if root is null     # return 0 for null node
2. left_depth = maximum_depth(root.left)
3. right_depth = maximum_depth(root.right)
4. return max(left_depth, right_depth) + 1  # return depth of the subtree rooted at root
```

##### How to decide the method?
1. Top-down
- You can determine some parameters to help the node know its answer.
- You can use these parameters and the value of the node itself to determine what should be the parammeters passed to its children.

2. Bottom-up
- For a node in tree, if you know the answer of its children, you can calculate the answer of that node.

