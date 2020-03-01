/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = nums => {
  if (!nums.length) {
    return 0;
  }

  let maxValue = nums[0];
  let prevValue = nums[0];
  for (let i = 1; i < nums.length; i++) {
    // If the previous value is more than 0, add it
    // Otherwise its a deadweight, just evaluate current number
    prevValue = nums[i] + (prevValue > 0 ? prevValue : 0);
    maxValue = Math.max(prevValue, maxValue);
  }

  return maxValue;
};
