class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isDigit(token):
                number = -int(token[1:]) if token[0] == "-" else int(token)
                stack.append(number)
            else:
                # b gets popped out first
                b = stack.pop()
                if token == "+":
                    stack[-1] += b
                elif token == "-":
                    stack[-1] -= b
                elif token == "*":
                    stack[-1] *= b
                else:
                    stack[-1] = stack[-1] / b
                    if stack[-1] < 0: stack[-1] = math.ceil(stack[-1])
                    else: stack[-1] = math.floor(stack[-1])
        return stack[0]

    def isDigit(self, token):
        if token.isdigit(): return True
        if len(token) > 1 and token[0] == "-": return token[1:].isdigit()
