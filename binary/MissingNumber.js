/**
 * @param {number[]} nums
 * @return {number}
 */
const missingNumber = nums => {
  // sum of n: n * (n + 1) / 2
  const n = nums.length;
  const sumTillN = n * (n + 1) / 2;
  const sumOfNums = nums.reduce((acc, num) => acc + num);
  return sumTillN - sumOfNums;
};
