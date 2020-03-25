/**
 * @param {number[]} nums
 * @return {number}
 */
const lengthOfLIS = nums => {
  if (!nums || !nums.length) return 0;
  const lookup = new Array(nums.length).fill(1);
  let max = 1;
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] <= nums[j]) continue;
      lookup[i] = Math.max(lookup[j] + 1, lookup[i]);
      max = Math.max(lookup[i], max);
    }
  }
  return max;
};

// Everytime we increment i, j gets reseted
// Math.max, take a look at [0,1,-1,2]. When its comparing 2 and -1, lookup[3] is already 3. If we don't take the max, we might just overwrite this value
// Lookup intent: Up until tile i, whats the longest increasing subsequence?
// [10,9,2,5,3,7,101,18] => [1,1,1,2,2,3,4,4]
