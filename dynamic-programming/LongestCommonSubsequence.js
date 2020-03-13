/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
const longestCommonSubsequence = (text1, text2) => {
  if (!text1 || !text1.length || !text2 || !text2.length) return 0;
  const m = text1.length;
  const n = text2.length;
  const lookup = new Array(m + 1);
  for (let i = 0; i <= m; i++) {
    if (!i) lookup[i] = new Array(n + 1).fill(0);
    else lookup[i] = new Array(n + 1);
    lookup[i][0] = 0;
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      lookup[i][j] = Math.max(lookup[i - 1][j], lookup[i][j - 1]);
      if (text1[i - 1] === text2[j - 1]) {
        lookup[i][j] = Math.max(lookup[i][j], lookup[i - 1][j - 1] + 1);
      }
    }
  }
  // To obtain, follow the diagonal until 1, go up to find left then up
  return lookup[m][n];
};
