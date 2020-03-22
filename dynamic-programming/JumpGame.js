/**
 * @param {number[]} nums
 * @return {boolean}
 */
// O(n)
const canJump = nums => {
  if (!nums || !nums.length) return false;
  let lastPos = nums.length - 1;
  for (let i = nums.length - 2; i >= 0; i--) lastPos = i + nums[i] >= lastPos ? i : lastPos;

  return !lastPos;
};

// O(n^2), but we don't really need the lookup
const canJumpSquaredTime = nums => {
  if (!nums || !nums.length) return false;
  const lookup = new Array(nums.length).fill(0);
  lookup[nums.length - 1] = 1;
  for (let i = nums.length - 2; i >= 0; i--) lookup[i] = Math.max(...lookup.slice(i, i + nums[i] + 1));

  return !!lookup[0];
};


/*
[2,4,2,1,0,2,0] length = 7
[0,0,0,0,0,0,1] i = 6
[0,0,0,0,0,0,1] i = 5, Math.max(nums.slice() = 5, 6, (7 no)
[1,1,0,0,0,1,1] i = 0, Math.max(lookup.slice(i, i + nums[i]))
*/
