/**
 * @param {number[]} nums
 * @return {number}
 */
const rob = nums => {
  if (!nums || !nums.length) return 0;
  if (nums.length < 2) return nums[0];

  let prev = nums[0];
  let curr = Math.max(nums[0], nums[1]);
  for (let i = 2; i < nums.length; i++) {
    [curr, prev] = [Math.max(prev + nums[i], curr), curr];
  }
  return curr;
};

const nonOptimizedRob = nums => {
  if (!nums || !nums.length) return 0;
  if (nums.length < 3) return Math.max(...nums);

  const lookup = new Array(nums.length);
  lookup[0] = nums[0];
  lookup[1] = Math.max(nums[0], nums[1]);
  for (let i = 2; i < nums.length; i++) {
    // Either rob (curr + prev 2), or don't rob (take prev)
    lookup[i] = Math.max(lookup[i - 1], lookup[i - 2] + nums[i]);
  }
  return lookup[lookup.length - 1];
};
