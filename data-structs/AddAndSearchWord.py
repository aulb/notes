from collections import defaultdict
class WordNode:
    def __init__(self):
        self.children = collections.defaultdict(WordNode)
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        prev = self.root
        for s in word:
            prev = prev.children[s]
        prev.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.result = False
        self.dfs(node, word)
        return self.result


    # WTF? ok
    def dfs(self, node: WordNode, word: str) -> None:
        if not word:
            if node.isEnd: self.result = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node: return
            self.dfs(node, word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True
            

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: return False
            node = node.children[char]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: return False
            node = node.children[char]
        return True

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.searchHelper(self.trie.root, word)
    
    def searchHelper(self, node: TrieNode, word: str) -> True:
        for index, char in enumerate(word):
            if char == ".": 
                for key in node.children:
                    if self.searchHelper(node.children[key], word[index + 1:]): return True
                return False
            else:
                if char not in node.children: return False
                node = node.children[char]
        return node.isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)