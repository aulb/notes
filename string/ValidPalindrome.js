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
