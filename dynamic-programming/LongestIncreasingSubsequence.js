/**
 * @param {number[]} nums
 * @return {number}
 */
const lengthOfLIS = nums => {
  if (!nums || !nums.length) return 0;
  const lookup = new Array(nums.length).fill(1);
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] <= nums[j]) continue;
      lookup[i] = Math.max(lookup[j] + 1, lookup[i]);
    }
  }
  return Math.max(...lookup);
};

// Everytime we increment i, j gets reseted
// Math.max, take a look at [0,1,-1,2]. When its comparing 2 and -1, lookup[3] is already 3. If we don't take the max, we might just overwrite this value
