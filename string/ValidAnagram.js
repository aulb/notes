// This is lookup for unicode
const makeLookup = string => {
  const lookup = {};
  for (let char of string) lookup[char] = lookup[char] ? lookup[char] + 1 : 1;
  return lookup;
}

// Lookup for lowercase letters only
const makeLowercaseLookup = string => {
  const lookup = new Array(26).fill(0);
  const base = 'a'.charCodeAt(0);
  for (let char of string) {
    const code = char.charCodeAt(0);
    lookup[code - base]++;
  }
  return lookup;
}

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = (s, t) => {
  const sLookup = makeLowercaseLookup(s);
  const tLookup = makeLowercaseLookup(t);

  for (let i = 0; i < 26; i++) {
    if (sLookup[i] !== tLookup[i]) return false;
  }
  return true;
};

/*
For unicode:
1) Make counter
2) Union, if not same length -> return false, because mismatch keys
3) For each key -> if not same value return false
*/
