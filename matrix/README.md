# Set Matrix Zeroes
1) Brute Force: `O(MN)` time and `O(M+N)` space. Use hashmap to keep track of the rows and cells needed to be zeroed out.
2) Brute Force Constant Space: Use `MODIFIED` which is an unused constant/integer to mark cells to be zeroed out. `O(MN * (M+N))` time. Extremely inefficient.
3) Build on top of the second solution. Postpone setting row and column to zero, instead mark the row/column that needed to be zeroed out.
```
if (!cell[i][j]) {
  cell[i][0] = 0; // Mark first cell of row as 0
  cell[0][j] = 0; // Mark first cell of column as zero
}
```
However the `cell[0][0]` is special and thus need an extra care.
Start iterating from `cell[1][1]`. Lastly check if `cell[0][0]` is zero and finish off.

# Word Search
This is NOT a simple DFS or BFS. Its more complicated.
Using tries are too complicated.

Remember to not be wasteful.
`word_to_find: ABCD` first letter: `C` then skip everything.
The solution I use uses no extra storage to track `wordSoFar`, instead it modifies the matrix

Runtime: O(nm) n = element in matrix, m = element in word
The naive implementation has a way nastier runtime.

# Search in 2D Matrix II
O(m + n), start at diagonal end thats not max/min.

# Spiral Matrix
Do one more spiral matrix example.
