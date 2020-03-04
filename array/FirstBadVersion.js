/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
const solution = isBadVersion => {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   * true true => go left
   * true false => return
   * false false => go right
   */
  const whichBadVersion = n => {
    let latest = n;
    let earliest = 1;
    while (latest >= earliest) {
      const middle = Math.floor((latest + earliest) / 2);
      if (isBadVersion(middle)) {
        if (!isBadVersion(middle - 1)) return middle;
        latest = middle - 1;
      } else {
        earliest = middle + 1;
      }
    }
    return 0;
  };
  return whichBadVersion;
};
