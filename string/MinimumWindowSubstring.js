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
  let charLeft = t.length;
  let foundAll = false;
  let l = 0;
  let r = 0;

  // Build counter
  const lookup = {};
  for (let char of t) {
    lookup[char] = lookup[char] ? lookup[char] + 1 : 1;
  }

  // Advance right while the charLeft is not 0 (meaning not all characters are found)
  // while (!(left < s.length || right < s.length)) {
  //   const currChar = charactersLeft ? s[left] : s[right];

  //   if (typeof tMap[currChar] === 'number') {
  //     if (tMap[currChar] > 0) {
  //       charactersLeft--;
  //     }
  //   }

  //   if (charactersLeft) {
  //     right++;
  //   } else {
  //     left++;
  //   }
  // }

  return foundAll ? minWindow : '';
};
