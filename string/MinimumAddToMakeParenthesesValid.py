class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closeBracketMiss = 0
        openBracketCount = 0
        for c in s:
            if c == "(":
                openBracketCount += 1
            else:
                if openBracketCount:
                    openBracketCount -= 1
                else:
                    closeBracketMiss += 1
        return closeBracketMiss + openBracketCount
    
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for char in S:
            if not stack:
                stack.append(char)
                continue
            if char == '(': stack.append(char)
            if char == ')':
                if stack[-1] == '(': stack.pop()
                else: stack.append(char)
        return len(stack)
