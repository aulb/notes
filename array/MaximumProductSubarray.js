/**
 * @param {number[]} nums
 * @return {number}
 */
const maxProduct = nums => {
  if (!nums || !nums.length) return 0;

  let maxValue = nums[0];
  let currValue = nums[0];
  let negativeHolder = nums[0] < 0 ? nums[0] : 1; // ???
  for (let i = 1; i < nums.length; i++) {
    const temp = currValue * nums[i];
    if (temp > 0) {
      currValue = temp;
    } else if (temp < 0) {
      currValue = 0;
    } else {
      currValue = nums[i];
    }
    // [-2,0,-1], if we skip 0, we might not record what the max value actually is
    maxValue = Math.max(maxValue, currValue);
  }
  return maxValue;
};
