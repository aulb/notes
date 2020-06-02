const getKey = r => `${r[0]}-${r[1]}-${r[2]}`;
/**
 * @param {number[]} nums
 * @return {number[][]}
 */

const threeSum = nums => {
  if (!nums || nums.length < 3) return [];
  nums.sort((a, b) => a - b);
  const res = [];
  // O(n^2) but don't check behind
  for (let i = 0; i < nums.length - 2; i++) {
    let l = i + 1;
    let r = nums.length - 1;
    while (l < r) {
      const total = nums[i] + nums[l] + nums[r];

      if (total < 0) l++;
      else if (total > 0) r--;
      else {
        res.push([nums[i], nums[l], nums[r]]);
        // TRY NOT to add duplicate, move pointers away from duplicates something like this: [1,1,2,4,3,3]
        while (l < r && nums[l] === nums[l + 1]) l++;
        while (l < r && nums[r] === nums[r - 1]) r--;
        l++;
        r--;
      }
    }
  }

  // Get rid of duplicates
  const lookup = {};
  return res.filter(r => {
    if (!lookup[getKey(r)]) {
      lookup[getKey(r)] = true;
      return true;
    }
    return false;
  });
}

/**
// TIME LIMIT EXCEEDED. But works :)
// 3Sum to a + b + c = 0
const threeSum = nums => {
  if (!nums || nums.length < 3) return [];
  const result = [];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length - 2; i++) {
    const twoSums = twoSum(nums.slice(i + 1), nums[i] * -1);
    if (!twoSums.length) continue;
    twoSums.forEach(A => result.push([nums[i], ...A]));
  }

  // Get rid of duplicates
  const lookup = {};
  return result.filter(r => {
    if (!lookup[getKey(r)]) {
      lookup[getKey(r)] = true;
      return true;
    }
    return false;
  });
};

const twoSum = (nums, target) => {
  if (!nums || !nums.length) return [];
  const result = [];
  const lookup = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (typeof lookup[target - num] === 'number') result.push([nums[i], nums[lookup[target - num]]]);
    lookup[num] = i;
  }
  return result;
};
 */
