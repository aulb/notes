/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
const reverseBits = n => {
  let result = 0;
  let count = 32; // 32 or 64 bit system
  while (count--) {
    result *= 2; // Make space for incoming bit -> 001 => 010
    result += n & 1; // Add the bit from n -> 010 -> 011
    n = n >> 1; // Shift n to examine the next bit, -> i.e 010 -> 001
  }
  return result;
};
