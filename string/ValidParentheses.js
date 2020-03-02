/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = s => {
  const openBrackets = [];
  const brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  };

  for (let char of s) {
    // if its an open bracket -> add
    if (brackets[char]) {
      openBrackets.push(char);
    } else {
    // if its a close bracket -> pop from top
      const openParanthes = openBrackets.pop();
      if (!openParanthes) return false;
      if (char !== brackets[openParanthes]) return false;
    }
  }

  return openBrackets.length === 0;
};
