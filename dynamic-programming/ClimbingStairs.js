/**
 * @param {number} n
 * @return {number}
 * fib(n)
 */
const climbStairs = n => {
  if (n < 2) return 1;
  let prev = 1; // 0
  let curr = 1; // 1
  for (let i = 2; i <= n; i++) [prev, curr] = [curr, curr + prev];
  return curr;
};
