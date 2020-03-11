/**
 * @param {number[]} nums
 * @return {number}
 */
 /*
class Solution(object):
  def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    # Takeaways, zeroes are sequence enders
    # min is the placeholder, carries the minimum up to this sequence
    # [2,3,0,4,8]
    # max: 2, 6, 0, 4, 32
    # min: 2, 3, 0, 4, 8 -> it doesn't even matter
    # [2,3,-1,4,8,-2]
    # max: 2, 6, -1, 4, 32
    # min: 2, 6, -6, -24, -192
    max_product = min_so_far = max_so_far = nums[0]

    for index in range(1, len(nums)):
      num = nums[index]
      if num < 0: min_so_far, max_so_far = max_so_far, min_so_far
      max_so_far = max(max_so_far * num, num)
      min_so_far = min(min_so_far * num, num)
      max_product = max(max_product, max_so_far)

    return max_product
 */
const maxProduct = nums => {
  if (!nums || !nums.length) return 0;

  let maxValue = nums[0];
  let maxSoFar = nums[0];
  let minSoFar = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];
    if (num < 0) {
      [minSoFar, maxSoFar] = [maxSoFar, minSoFar];
    }
    maxSoFar = Math.max(maxSoFar * num, num);
    minSoFar = Math.min(minSoFar * num, num);
    maxValue = Math.max(maxValue, maxSoFar);
  }

  return maxValue;
};
