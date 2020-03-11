/**
 * @param {number[]} nums
 * @return {number}
 */
const rob = nums => {
  if (!nums ||!nums.length) return 0;
  if (nums.length < 4) return Math.max(...nums);
  return Math.max(helper(nums.slice(0, nums.length - 1)), helper(nums.slice(1, nums.length)));
}

const helper = nums => {
  if (!nums || !nums.length) return 0;
  if (nums.length < 2) return nums[0];

  let prev = nums[0];
  let curr = Math.max(nums[0], nums[1]);
  for (let i = 2; i < nums.length; i++) {
    [curr, prev] = [Math.max(prev + nums[i], curr), curr];
  }
  return curr;
};
