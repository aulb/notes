/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const moveZeroes = nums => {
  if (!nums || !nums.length) {
    return;
  }
  
  let slow = 0;
  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast]) {
      [nums[fast], nums[slow]] = [nums[slow], nums[fast]];
      slow++;
    }
  }
  return nums;
};