# Binary Trees
Just a regular two child'd tree y'all.
When it be searchin it needs to obey the rule (left small, right big).

# Breadth First Search
- Good to find a "shortest path"
- Uses a queue
```
set all nodes to "not visited"
q = new Queue();
q.enqueue(initialNode)
while (q != empty)
  x = q.dequeue();
  if (x not visited)
    set x to visited
    for every edge of x. call it y
      if y has not been visited
        q.enqueue(y)
```

# Depth First Search
- Tells us if a path even exists.
- Uses a stack instead

# Preorder, Inorder, Postorder traversals
Tree traversals
## Preorder: CURR, LEFT, RIGHT
The pre-order traversal is a topologically sorted one, because a parent node is processed before any of its child nodes is done.

## Inorder: LEFT, CURR, RIGHT
In a binary search tree ordered such that in each node the key is greater than all keys in its left subtree and less than all keys in its right subtree, in-order traversal retrieves the keys in ascending sorted order.

## Reverse: RIGHT, CURR, LEFT
Opposite of inorder (descending sorted order).

## Postorder: LEFT, RIGHT, CURR
