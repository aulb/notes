class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # is being used
        # keep track of index separately
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit again <-- use this technique..
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or \
        self.dfs(board, i-1, j, word[1:]) or \
        self.dfs(board, i, j+1, word[1:]) or \
        self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
    
######
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        # Words ["eat", "ear"]
        if node.isWord:
            res.append(path)
            # No duplicates
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return 
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp


class Solution:
    def __init__(self):
        self.direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.visited = '#'

    def existMultiple(self, board: List[List[str]], words: List[str]) ->: List[str]:
        result = []
        for word in words:
            if self.exists(board, word): 
                result.append(word)
        return result
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Basic check not extensive check, does not check if uniform list size inside the list
        if not len(board) or not len(board[0]): return False
        m, n = len(board), len(board[0])
        if not len(word) or len(word) > m * n: return False
        
        for i in range(m):
            for j in range(n):
                if self.helper(board, word, i, j): return True
        return False
    
    def helper(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        # Return condition 1: 
        if word[0] != board[i][j]: return False
        
        # Return condition 2:
        # Last letter is checked by the top condition
        if len(word) == 1: return True # Nothing else to check
        
        # Only "visit" when it is part of the word, otherwise whatever
        # Direction walk
        board[i][j] = self.visited
        for direction in self.direction:
            newI, newJ = i + direction[0], j + direction[1]
            if newI >= 0 and newI < len(board) and newJ >= 0 and newJ < len(board[0]) and self.helper(board, word[1:], newI, newJ): 
                board[i][j] = word[0]
                return True
        board[i][j] = word[0]
        return False
    
