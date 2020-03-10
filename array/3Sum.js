/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = nums => {

};

const twoSum = (nums, target) => {
  if (!nums || !nums.length) return [];
  const result = [];
  const lookup = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (typeof lookup[target - num] !== 'number')  result.push([i, lookup[target - num]]);
    lookup[num] = i;
  }
  return result;
};
