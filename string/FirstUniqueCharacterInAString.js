/**
 * @param {string} s
 * @return {number}
 */
const firstUniqChar = s => {
  if (!s) return -1;
  const lookup = {};

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (!lookup[char]) lookup[char] = { count: 0, index: i };
    lookup[char].count++;
  }

  let minIndex = Infinity;
  for (let char of Object.keys(lookup)) {
    minIndex = lookup[char].count === 1 ? Math.min(lookup[char].index, minIndex) : minIndex;
  }

  return minIndex === Infinity ? -1 : minIndex;
};
