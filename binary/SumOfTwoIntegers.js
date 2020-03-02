/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
const getSum = (a, b) => {
  if (b === 0) return a;
  // a XOR b, a OR b shift 1. XOR-ing works because its like adding.
  // 0 + 0 => 0
  // 1 + 1 => 0 (1 carried over)
  // 0 + 1 => 1
  // The goal is to get to the base case of (a = num, b = 0).
  return getSum(a ^ b, (a & b) << 1);
};
