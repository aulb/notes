/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number} // Only returning min number needed to make
 */
const coinChange = (coins, amount) => {
  const lookup = new Array(amount + 1).fill(Infinity); // to account for 0
  lookup[0] = 0;
  for (let coin of coins) {
    for (let i = coin; i < lookup.length; i++) {
      lookup[i] = Math.min(lookup[i], 1 + lookup[i - coin]);
    }
  }
  return lookup[amount] === Infinity ? -1 : lookup[amount];
};

// EXTRA! And also all unique values
const noCoin = -1;
const getCoinChange = (coins, amount) => {
  const lookup = new Array(amount + 1).fill(Infinity);
  const coinLookup = new Array(amount + 1).fill(noCoin);

  for (let i = 0; i < coins.length; i++) {
    const coin = coins[i];
    for (let j = coin; j < lookup.length; j++) {
      if (lookup[j - coin] + 1 > lookup[j]) {
        coinLookup[j] = coin;
        lookup[j] = lookup[j - coin] + 1;
      }
    }
  }

  let leftover = amount;
  const coinChange = [];
  while (coinLookup[leftover] !== noCoin) {
    coinChange.push(coinLookup[leftover]);
    leftover = leftover - coinLookup[leftover];
  }
  return coinChange;
};
