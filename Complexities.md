Algorithm runtimes and complexities + explanations.
# Data Structures
## Heap / PQ [Array Representation]
Insert - `O(logn)` (`n` the size of the current tree)
Heapify - `O(logn)` - called in a top down manner
## Binary Search Tree
Unbalanced binary search tree always have `O(n)` as its worst case scenario.
Rebalancing a binary tree helps with keeping everything `O(logn)`



# Sorting Algorithms
Todo.

# Search Algorithms
## DFS/BFS
General runtime: `O(V + E)`. Vertices and edges. Matrix DFS algo
``` # Concrete example
[1,2,3]
[4,5,6] => 9 vertices, if edges is up, left, down, right then 24 edges (max 36 edges)
[7,8,9]
```
**Topological Sort**
Can be done with DFS or BFS doesn't matter. Finds cycles.

# General Explanation
[Link](https://algs4.cs.princeton.edu/cheatsheet/)
