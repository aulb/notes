# Same Tree
Simple left right checks. DFS pretty much.

# Construct Binary Tree from Preorder and Inorder Traversals
[Read explanation](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34538/My-Accepted-Java-Solution)

# Is Valid Binary Search Tree
*REMEMBER* That we need to check for max and min of the whole tree as well.
`[10,5,15,null,null,6,20]`

# Kth Smallest Element
k = 1 means smallest. All the element to the left are smallest, if k is lesser than count of left nodes, its on the left. If its bigger, then its on the right.

Basically counting left/right nodes.

# LCA
First in between is always the lowest common ancestor. By BST property. Also read the function signature!
