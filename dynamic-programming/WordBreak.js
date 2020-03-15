/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = (s, wordDict) => {
  if (!s || !s.length || !wordDict || !wordDict.length) return false;

  // The lookup is "is there a substr that can be made with the word dict?"
  const lookup = new Array(s.length).fill(false);
  for (let i = 0; i < s.length; i++) {
    for (let word of wordDict) {
      // i = 0, "hello" "he" => "_h"
      if (i - word.length + 1 < 0) continue;

      if (s.substr(i - word.length + 1, word.length) === word &&
        // beginning of s
        (i - word.length === -1 ||
        // a substr up until lookup[i - word.length] can be made with word dict
        lookup[i - word.length])
      ) lookup[i] = true;
    }
  }

  return lookup[lookup.length - 1];
};

/* Quick lookup
aplepen, [aple, pen]
[0,0,0,1,0,0,1]
*/
