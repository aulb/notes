/**
 * @param {string} s
 * @return {number}
 */
/*
Middle of palindrome could be in one of 2n - 1 positions.
"abba"
"a", "b", "b", "a" could be centers
"a _ b", "b _ b", "b _ a" the middle of two letters could be centers
(l,r) => [
  (0,0), // center 0, l = center / 2 --> 0, r = l + c % 2
  (0,1),
  (1,1),
  ...
];
*/
const countSubstrings = s => {
  if (!s || !s.length) return 0;
  const n = s.length;

  let result = 0;
  for (let center = 0; center < 2 * n - 1; center++) {
    let l = Math.floor(center / 2);
    let r = l + center % 2; // 0, 0 or 0, 1
    while (l >= 0 && r < n && l <= r && s[l] === s[r]) {
      l--;
      r++;
      result++;
    }
  }

  return result;
};
