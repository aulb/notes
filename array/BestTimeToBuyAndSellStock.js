/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = prices => {
  if (!prices.length ) return 0;

  let currLow = prices[0];
  let currHigh = prices[0];
  let maxProfit = currHigh - currLow;
  let currProfit = maxProfit;
  for (let price of prices) {
    if (price < currLow) {
      currLow = currHigh = price;
      continue;
    }

    if (price > currHigh) {
      currHigh = price;
    }

    currProfit = currHigh - currLow;
    maxProfit = Math.max(maxProfit, currProfit);
  }

  return maxProfit;
};
