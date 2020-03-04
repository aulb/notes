# Set Zeroes
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