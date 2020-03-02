/**
 * @param {string} s
 * @return {boolean}
 */
const validPalindrome = s => {
  if (!s) return true;

  const string = s.replace(/\W/g, '').toLowerCase();
  let front = 0;
  let back = string.length - 1;
  while (back >= front) {
    if (string[front] !== string[back]) {
      const string1 = string.substring(0, front) + string.substring(front + 1);
      const string2 = string.substring(0, back) + string.substring(back + 1);
      return isPalindrome(string1) || isPalindrome(string2);
    }

    front++;
    back--;
  }
  return true;
};

/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = s => {
  if (!s) return true;

  const string = s.replace(/\W/g, '').toLowerCase();
  let front = 0;
  let back = string.length - 1;
  while (back >= front) {
    if (string[front] !== string[back]) return false;
    front++;
    back--;
  }
  return true;
};
