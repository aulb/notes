/**
 * @param {number} K // Eggs
 * @param {number} N // Floors
 * @return {number}
 */
const superEggDrop = (K, N) => {
  const lookup = new Array(K);
  for (let i = 0; i < K; i++) lookup[i] = new Array(N);
  for (let i = 0; i < N; i++) lookup[0][i] = i + 1;

  // Iterate through number of eggs
  for (let egg = 1; egg < K; k++) {
    for (let n = 0; n < N; n++) {
      // If theres more eggs than there are floors, same as previous egg set
      if (egg > n) {
        lookup[egg][n] = lookup[egg - 1][n];
        continue;
      }

      // Otherwise test egg drop from each floor
      let min = Infinity;
      for (let floor = 0; floor < n; floor++) {
        // We know with certainty only on the first and last floor
        // If it breaks on the first floor --> done
        // If it doesn't break on the last floor --> done
        min = Math.min(min, 1 + Math.max(
          // Case where it breaks, we have one less egg
          floor === 0 ? 0 : lookup[egg - 1][floor],
          // Case where it does not break, we have n - 1 floor left to go
          floor === n - 1 ? lookup[egg][n - (floor + 1)] : 0,
        ));
      }
      lookup[k][n] = min;
    }
  }

  console.log({lookup});
  return lookup[K - 1][N - 1];
};
