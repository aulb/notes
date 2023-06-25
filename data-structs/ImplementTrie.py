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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# MISTAKE; The root shouldn't be a dict. A single root where you track the node is ok
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.children = {}


    def getInitialNode(self, word: str, shouldCreate: bool) -> TrieNode:
        if not word: return None
        prevNode = self.children.get(word[0], None)
        if prevNode is None and shouldCreate:
            prevNode = TrieNode(word[0])
            self.children[word[0]] = prevNode
        return prevNode
            

    def insert(self, word: str) -> None:
        if not word: return
        prevNode = self.getInitialNode(word, True)
        for index in range(1, len(word)):
            char = word[index]
            childNode = prevNode.children.get(char, None)
            if childNode is None:
                childNode = TrieNode(char)
                prevNode.children[char] = childNode
            prevNode = childNode
        prevNode.isEndOfWord = True
            

    def search(self, word: str) -> bool:
        if not word: return False
        prevNode = self.getInitialNode(word, False)
        if prevNode is None: return False
        for index in range(1, len(word)):
            char = word[index]
            childNode = prevNode.children.get(char, None)
            if childNode is None: return False
            prevNode = childNode
        return prevNode.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return False
        prevNode = self.getInitialNode(prefix, False)
        if prevNode is None: return False
        for index in range(1, len(prefix)):
            char = prefix[index]
            childNode = prevNode.children.get(char, None)
            if childNode is None: return False
            prevNode = childNode
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)