/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = (nums, target) => {
  /*
  // Sorted
  Normal binary search
  1,2,3,4,5 = l,m,h

  // Not sorted 1. but the left side is sorted
  2,3,4,5,1 = m,h,l
  3,4,5,1,2 = m,h,l

  // Not sorted 2. but the right side is sorted
  4,5,1,2,3 = h,l,m
  5,1,2,3,4 = h,l,m
  */
  if (!nums || !nums.length) {
    return -1;
  }

  let left = 0;
  let right = nums.length - 1;
  while (right >= left) {
    const mid = Math.floor((right + left) / 2);
    if (nums[mid] === target) return mid;

    // Case 1, sorted on the left side
    if (nums[mid] >= nums[left]) {
      // Check if the target is on the left side
      // Equal cause it can also be nums[right] itself
      if (nums[mid] > target && target >= nums[left]) {
        right = mid - 1;
      } else {
        // On the right side
        left = mid + 1;
      }
    // Case 2, sorted on the right side
    } else if (nums[right] >= nums[mid]) {
      if (target > nums[mid] && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
};
