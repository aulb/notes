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

Idea (from discussion on lc):
- Widest container is always a good candidate and what we start with
- Every other container is less wide, we need a higher tower to hold more water
- The smaller one of the first and last doesn't support higher water level, can be removed

One consideration: if `h[i] === h[j]`, we need to prove that it doesn't matter if `i++` or `j--`.
Answer:
You need to prove that in this case, it does not matter whether you perform `i++` or `j--`, because if `h[i] == h[j]`, neither `(i+1, j)` or `(i, j-1)` can be potential solutions because the area obtained is necessarily smaller than `(i, j)`.

# First Bad Version
*FACEBOOK* question.

# Two Sum
Given nums = [2, 11, 7, 15], target = 9,
Is there a 7? No? Ok 2 is at 0.
Is there a -2? No? Ok 11 is at 1.
Is there a 2? Yes! 2 is at 0, 7 is at 2. Done.

# 3Sum
Why can I only check the rest of the array? Because suppose the PREVIOUS number in the iteration is included, then during finding the two sum, we should've found something
[Explanation](https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained))

# Task Scheduler
Was asked by "Rbrc".
Think outside the box, the solution is simpler than you think.
Outside the box: Each tasks does NOT have to be executed right when the cooldown is done.

# Subarray Sum Equals K
We can always generate all possible subarray in O(n^2) time. For each subarray, calculate the sum and see if it matches with the target `k`. Runtime is O(n^3).

To bring it down to O(n^2), we can call upon a useful technique and make a cumulative sum array. We can use this cumulative sum array to calculate the value between to indices.
`sum(nums between 1 to 3]) = cumulativeSum at index 3 - cumulativeSum at index 1`.
Now we can iterate the same way as before and up the count.

To bring it down to linear time.
*Cumulative sum up to two indices, say **i** and **j** is at a difference of **k**.*
*Further, for every sum encountered, we also determine the number of times the sum `sum - k` has occured already, since it will determine the number of times a subarray with sum `k` has occured up to the current index. We increment the count by the same amount.*
i.e: We can make two different subarrays with sum `k` at index `i`.

# Find First and Last Position of Element in Sorted Array
Binary search continuosly on the left and right on target (once found).

# Longest Consecutive Sequence
Remember hash map, your best friend. A quick lookup that saves a lot of time. Subsequence really.
Find the start of the sequence and keep going.

# Trapping Rain Water
The classic left right array lookups.
Brute force: For every num (except first and last), keep moving to the right until it finds an element thats equal or bigger than. Every num passed is smaller (calculate the water trapped)

# Sliding Window Maximum
Keep a deque (popleft and appendleft O(1) arrays). The value of the zeroeth element is the index of the current max number.
When appending to the deque, sweep from end and pop everything that isn't bigger than itself.
The reason this is still linear runtime is because all the element is queued and dequeued at least once.
