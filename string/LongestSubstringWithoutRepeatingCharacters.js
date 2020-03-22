/**
 * @param {string} s
 * @return {number}
 */
/*
abca, a, b, c

Define: We want l and r to be the boundary where all the characters in it (inclusive)
are unique.

Mark the character as found, whenever new are found.
If we found a duplicate, find the duplicate with l. Mark every char as not found as
we increment l. Once found, increment up to make sure the boundary stays sane.
*/
const lengthOfLongestSubstring = s => {
  if (!s || !s.length) return 0;

  let l = 0;
  let max = 0;
  const lookup = { };
  for (let r = 0; r < s.length; r++) {
    // If haven't discovered, mark as discovered
    if (!lookup[s[r]]) lookup[s[r]] = true;
    else {
      while (s[l] !== s[r] && l <= r) {
        lookup[s[l]] = false;
        l++;
      }
      l++;
    }

    max = Math.max(r - l + 1, max);
  }

  return max;
};
