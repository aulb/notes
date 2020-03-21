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

const makeKey = lookupArray => lookupArray.join('-');

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = strs => {
  const map = {};
  for (let s of strs) {
    const lookup = makeLowercaseLookup(s);
    const key = makeKey(lookup);
    if (!map[key]) map[key] = [];
    map[key].push(s);
  }

  const result = [];
  for (let key of Object.keys(map)) result.push(map[key]);
  return result;
};

/*
Note for unicode:
1) Make counter object
2) Make a good unique key, maybe something ordered like charCodeAt (needs sorting)
3) Push to map and then extract from map
*/
