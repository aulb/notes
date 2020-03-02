# Best Time to Buy and Sell Stock
Buy low sell high.
Everytime our stock price is higher, we will try to "sell".
Everytime we encounter a new lowest price point, we buy and start new.

# Product of Array Except Self
With division: beware of 0s in the array.
Without division: Make left or right array. Left at index `i` meaning the product of all the numbers to the left of index `i`.

# Contains Duplicate
Literally just use hash map. Unless its the values are between `[1, array.length]`, no tricks are needed.

# Maximum Subarray
We always need to see what the value of current number in the iteration plus its previous one.
We only care about the previous value if its greater than 0.

# Maximum Product Subarray

# Find Minimum in Rotated Sorted Array
Needed: Binary search mastery.
```
/**
 * Note: Boundary: [l, h)
 * Floor because I am doing l = m + 1. Need to keep everything in bound.
 * Ceiling would cause it to go out of bound, skipping some elements.
 */
const binarySearch = (array, target) => {
  const n = array.length;
  let h = n;
  let l = 0;
  let m = Math.floor((h + l) / 2);

  while (m >= l && m < h) {
    const currValue = array[m];
    if (currValue === target) return m;
    if (currValue < target) l = m + 1;
    if (currValue > target) h = m;
    m = Math.floor((h + l) / 2);
  }

  return -1;
};
```
