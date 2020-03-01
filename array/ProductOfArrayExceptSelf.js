/**
 * @param {number[]} nums
 * @return {number[]}
 */
const productExceptSelf = nums => {
  const n = nums.length;
  const l = new Array(n).fill(1);
  const r = new Array(n).fill(1);
  let j = n - 1;
  for (let i = 0; i < n; i++) {
    // Prevent oob errors
    // Current neighbour you can get from the original nums array
    const currL = i - 1 >= 0 ? nums[i - 1] : 1;
    // Previous value (the product) we can get from the left/right array
    const prevL = i - 1 >= 0 ? l[i - 1] : 1;
    l[i] = currL * prevL;

    const currR = j + 1 < n ? nums[j + 1] : 1;
    const prevR = j + 1 < n ? r[j + 1] : 1;
    r[j] = currR * prevR;
    j--;
  }

  return nums.map((_, idx) => l[idx] * r[idx]);
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const productExceptSelfWithDivision = nums => {
  if (!nums || !nums.length) {
    return [];
  }

  // Division by 0, beware. [1,0], [1,2,3,0] => a 6 is possible, [1,0,2,0] => 0
  const numOfZeroes = nums.filter(num => !num).length;
  const productOfAll = nums.reduce((acc, num) => acc * num);
  const productOfAllWithoutZero = nums.reduce((acc, num) => num ? acc * num : acc);

  return nums.map(num => {
    // If theres more than one zeroes, the entire array will be 0
    if (numOfZeroes > 1) return 0;

    // If theres only one or none then return just the product divided by self
    if (num) return productOfAll / num;
    return productOfAllWithoutZero;
  });
};
