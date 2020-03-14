/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = (nums1, m, nums2, n) => {
  if (!nums1 || !nums2 || !nums2.length) return;
  // EDGE CASE: [0], 0, [1], 1. Don't change the logic below because to use nums1[i] === 0
  // Simple swap approach works for m === n ONLY.

  // This approach works by going from behind, and gradually pushing the numbers
  // greater than the one being compared to the back of the list
  // No need to swap, we don't care about the 0s
  while (n > 0) {
    if (m <= 0 || nums2[n - 1] >= nums1[m - 1]) {
      nums1[m + n - 1] = nums2[n - 1]
      n--;
    } else {
      nums1[m + n - 1] = nums1[m - 1];
      m--;
    }
  }
};

/*
EDGE CASE 1: n1: [4,0,0,0] n2: [1,2,5], m = 1, n = 3
iter1: [4, 0, 0, 5]
iter2: [4, 0, 4, 5] m = 0, (m <= 0) so just copy the rest over from behind
iter4: [1, 2, 4, 5]

EDGE CASE 2: n1: [1,3,4,0] n2: [2] m = 3, n = 1
iter1: [1, 3, 4, 4] m = 2
iter2: [1, 3, 3, 4] m = 1
iter3: [1, 2, 3, 4] n = 0 done. once n is exhausted, the algorithm terminates (everything is sorted)
*/
