class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        output = []
        for word in words:
            if self.findWord(board, word): output.append(word)
        return output

    def findWord(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]: continue
                if self.dfs(board, word, i, j): return True
        return False

    def dfs(self, board, word, i, j):
        if len(word) == 0: return True
        # Check for return condition at the top
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]: return False
        temp = board[i][j]
        result = self.dfs(board, word[1:], i - 1, j) or \
        self.dfs(board, word[1:], i + 1, j) or \
        self.dfs(board, word[1:], i, j + 1) or \
        self.dfs(board, word[1:], i, j - 1) 
        board[i][j] = temp
        return result
