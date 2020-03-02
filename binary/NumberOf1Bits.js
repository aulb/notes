/**
 * @param {number} n - a positive integer
 * @return {number}
 */
const hammingWeight = n => {
  // Number of two exponents
  // Instead of counting that, lets do the trick.
  // n = 111
  // n - 1 = 110
  // This works because in binary rep, the least significant 1-bit in n alawys corresponds to 0-bit in n - 1.
  // It flips the least significant 1-bit in n to 0, but all other bits are the same.
  // Essentially work backwards.
  let sum = 0;
  while (n) {
    sum++;
    n = n & (n - 1);
  }
  return sum;
};
