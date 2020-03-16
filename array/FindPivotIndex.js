/**
 * @param {number[]} nums
 * @return {number}
 */
const pivotIndex = nums => {
  if (!nums || !nums.length) return -1;
  const sums = new Array(nums.length);
  for (let i = 0; i < nums.length; i++) {
    sums[i] = i > 0 ? sums[i - 1] + nums[i] : nums[i];
  }

  // Application of the cumulative sum
  for (let i = 0; i < nums.length; i++) {
    // Take care of edge cases, 0 and nums.length will compare with sum of 0
    if (!i && sums[nums.length - 1] - sums[i] === 0) return i;
    if (i === nums.length - 1 && sums[i - 1] === 0) return i;
    if (sums[nums.length - 1] - sums[i] === sums[i - 1]) return i;
  }

  return -1;
};
