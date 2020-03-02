/**
 * Assummed that the array is sorted.
 * No duplicates. Find pivot then find the min.
 * @param {number[]} nums
 * @return {number}
 */
const findMin = nums => {
  if (!nums.length) {
    return 0;
  }

  if (nums.length === 1) {
    return nums[0];
  }

/*
// Sorted
1,2,3,4,5 = l,m,h
// Not sorted 1
The minimum is on the right side
2,3,4,5,1 = m,h,l
3,4,5,1,2 = m,h,l
// Not sorted 2
The minimum is on the left side
4,5,1,2,3 = h,l,m
5,1,2,3,4 = h,l,m

Stopping condition is l < m < h
This condition: m < l < h is invalid (unsorted)
*/
  let r = nums.length - 1;
  let l = 0;
  if (nums[r] > nums[0]) {
    return nums[0];
  }

  while (r >= l) {
    const m = l + (r - l) / 2;
    if (nums[m] > nums[m + 1]) {
      return nums[m + 1];
    }

    if (nums[m - 1] > nums[m]) {
      return nums[m];
    }

    if (nums[mid] > nums[0]) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  return l;
};

const binarySearch = (array, target) => {
  const n = array.length;
  let r = n - 1;
  let l = 0;

  while (r >= l) {
    const m = l + (r - l) / 2;
    const currValue = array[m];
    if (currValue === target) return m;
    if (currValue < target) l = m + 1;
    if (currValue > target) r = m - 1;
  }

  return -1;
};
