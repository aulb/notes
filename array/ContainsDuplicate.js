/**
 * @param {number[]} nums
 * @return {boolean}
 */
// General, literally sort, or use hash map
const containsDuplicate = nums => {
  // ya ok there
};


/**
 * @param {number[]} nums
 * @return {boolean}
 */
const DUPLICATE_MAX_INT_FLAG = 2;
const containsDuplicateBetween1ToArrLength = nums => {
  // No hashes allowed
  // No array modification allowed? (this rule is terrible)
  // Rule 1: Integers between [1, array.length], no negatives
  let oob = 0;
  for (let num of nums) {
    if (num >= nums.length) {
      oob++;
      if (oob === DUPLICATE_MAX_INT_FLAG) {
        return true;
      }
      continue;
    }


    // Note: [1,2,3,1] => Second iter: [1,-2,3,1]
    const idx = Math.abs(num);
    if (nums[idx] < 0) return true;

    nums[idx] = nums[idx] * -1;
  }

  // Check for out of bound one last time, checking one last time is always important
  return oob === DUPLICATE_MAX_INT_FLAG;
};
