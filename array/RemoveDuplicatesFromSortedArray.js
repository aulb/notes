/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = nums => {
  if (!nums || !nums.length) return nums;
  let j = 0;
  let prev = nums[0];
  /*
  { nums: [ 1, 2, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6 ] }
  { nums: [ 1, 2, 3, 2, 2, 2, 1, 4, 5, 5, 5, 5, 6 ] }
  { nums: [ 1, 2, 3, 4, 2, 2, 1, 2, 5, 5, 5, 5, 6 ] }
  { nums: [ 1, 2, 3, 4, 5, 2, 1, 2, 2, 5, 5, 5, 6 ] }
  { nums: [ 1, 2, 3, 4, 5, 6, 1, 2, 2, 5, 5, 5, 2 ] }
  */
  for (let i = 1; i < nums.length; i++) {
    // If its different then j++, swap current with
    if (prev !== nums[i]) {
      j++;
      prev = nums[i];
      [nums[j], nums[i]] = [nums[i], nums[j]];
    }
  }
  return j + 1;
};
