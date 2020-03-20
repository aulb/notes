/**
 * @param {string} s
 * @return {string}
 */
const decodeString = s => {
  if (!s) return ''; // Assume all s is valid
  const { result } = helper(s, 0);
  return result;
};

// Return last index
const helper = (s, i) => {
  let decoded = '';
  let digit = 0;
  while (i < s.length && s[i] !== ']') {
    const char = s[i];

    // parseInt(char) !== NaN // char = 's' for example. This will be true
    // Use isNaN
    if (!isNaN(parseInt(char))) {
      digit = digit * 10 + parseInt(char);
      i++;
      continue;
    } else if (s[i] === '[') {
      const { finalI, result } = helper(s, i + 1);
      for (let x = 0; x < digit; x++) decoded = decoded + result;
      i = finalI;
      digit = 0;
      continue;
    }

    // Regular letter
    decoded = decoded + char;
    i++;
  }

  return { result: decoded, finalI: i + 1 };
};
