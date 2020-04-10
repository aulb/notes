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
