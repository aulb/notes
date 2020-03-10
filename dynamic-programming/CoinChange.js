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
const getCoinChange = (coins, amount) => {

};
