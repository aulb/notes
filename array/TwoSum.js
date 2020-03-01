/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function(nums, target) {
  const lookup = {};
  for (const idx in nums) {
    if (lookup[target - nums[idx]] >= 0) return [idx, lookup[target - nums[idx]]];
    lookup[nums[idx]] = idx;
  }
};
