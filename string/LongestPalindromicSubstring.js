/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = s => {
  if (!s || !s.length) return '';
  // A letter is a palindrome by default, maxLength of palindrome will start from 1
  let maxLen = 1;
  // Keep track of the start of the palindrome
  let start = 0;

  for (let i = 0; i < s.length; i++) {
    // Find odd cases like 'aba
    const oddCase = expandFromCenter(s, i, i);
    // Find even cases like 'abba'
    const evenCase = expandFromCenter(s, i, i + 1);
    const currMax = Math.max(oddCase, evenCase);
    if (currMax > maxLen) {
      maxLen = currMax;
      start = i - Math.floor((maxLen - 1) / 2);
    }
  }

  return s.substr(start, maxLen);
};

// This returns the max length;
const expandFromCenter = (s, l, r) => {
  if (!s || l > r) return 0;
  while (l >= 0 && r < s.length && s[l] === s[r]) {
    l--;
    r++;
  }
  return r - l - 1;
};
