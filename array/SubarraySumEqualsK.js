/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const subarraySum = (nums, k) => {
  if (!nums || !nums.length) return 0;
  let count = 0;
  let sum = 0;
  const lookup = {};
  lookup[0] = 1;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    if (lookup[sum - k]) count += lookup[sum - k];
    lookup[sum] = lookup[sum] ? 1 : lookup[sum] + 1;
  }

  return count;
};
