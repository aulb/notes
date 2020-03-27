/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = x => {
  const originalX = x;
  if (x < 0) return false;
  let compare = 0;
  while (x > 0) {
    compare = compare * 10 + x % 10;
    x = Math.floor(x / 10);
  }

  return compare === originalX;
};
