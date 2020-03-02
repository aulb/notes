/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
const minWindow = (s, t) => {
  let minWindow = '';
  if (!s.length) return minWindow;

  // Only decrease if the counter -- >= 0
  // Only increase if the counter ++ > 0
  let charactersLeft = t.length;
  let left = 0;
  let right = 0;

  // Build counter
  const tMap = {};
  for (let char of t) {
    tMap[char] = tMap[char] ? tMap[char] + 1 : 1;
  }

  while (!(left < s.length || right < s.length)) {
    const currChar = charactersLeft ? s[left] : s[right];

    if (typeof tMap[currChar] === 'number') {
      if (tMap[currChar] > 0) {
        charactersLeft--;
      }
    }

    if (charactersLeft) {
      right++;
    } else {
      left++;
    }
  }

  return minWindow;
};
