/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = prices => {
  if (!prices || prices.length < 2) return 0;

  let total = 0;
  for (let i = 1; i < prices.length; i++) {
    total += Math.max(0, prices[i] - prices[i - 1]);
  }
  return total;
};
