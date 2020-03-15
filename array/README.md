# Best Time to Buy and Sell Stock
Buy low sell high.
Everytime our stock price is higher, we will try to "sell".
Everytime we encounter a new lowest price point, we buy and start new.

# Product of Array Except Self
With division: beware of 0s in the array.
Without division: Make left or right array. Left at index `i` meaning the product of all the numbers to the left of index `i`.

# Move Zeroes
Fast and slow pointer. Slow to keep track of where the start of the zeros are.

# Contains Duplicate
Literally just use hash map. Unless its the values are between `[1, array.length]`, no tricks are needed.

# Maximum Subarray
We always need to see what the value of current number in the iteration plus its previous one.
We only care about the previous value if its greater than 0.

# Maximum Product Subarray

# Find Minimum in Rotated Sorted Array
Needed: Binary search mastery.
Need to keep the `while` condition simple. Right is bigger or equal to left.

# Search in Rotated Sorted Array
Its important inside the `while` to have a solid terminating condition.
Its possible that `left` and `right` to be the same. If its not `>=` then it will get an inf loop.

# Container with Most Water
[Solution Explanation](https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm).
"Greedy window".

# First Bad Version
*FACEBOOK* question.

# Two Sum
Given nums = [2, 11, 7, 15], target = 9,
Is there a 7? No? Ok 2 is at 0.
Is there a -2? No? Ok 11 is at 1.
Is there a 2? Yes! 2 is at 0, 7 is at 2. Done.

# 3Sum
Why can I only check the rest of the array?
[Explanation](https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained))

# Task Scheduler
Was asked by "Rbrc".
