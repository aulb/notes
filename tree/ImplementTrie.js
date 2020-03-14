/**
 * Initialize your data structure here.
 */
var Trie = function() {
  this.__word_end__ = '__word_end__';
  this.lookup = {};
};

/**
 * Inserts a word into the trie.
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
  let prevLookup = this.lookup;
  for (let char of word) {
    // Initialize hash for each letter
    if (!prevLookup[char]) prevLookup[char] = {};
    prevLookup = prevLookup[char];
  }
  prevLookup[this.__word_end__] = true;
};

/**
 * Returns if the word is in the trie.
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
  let prevLookup = this.lookup;
  for (let char of word) {
    if (!prevLookup[char]) return false;
    prevLookup = prevLookup[char];
  }
  return !!prevLookup[this.__word_end__];
};

/**
 * Returns if there is any word in the trie that starts with the given prefix.
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
  let prevLookup = this.lookup;
  for (let char of prefix) {
    if (!prevLookup[char]) return false;
    prevLookup = prevLookup[char];
  }
  return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
