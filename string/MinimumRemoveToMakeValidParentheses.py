class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return ""
        tracker = list(s)
        brackets = []
        for index, char in enumerate(s):
            if char == "(":
                tracker[index] = "" 
                brackets.append(index)
            elif char == ")":
                if brackets:
                    idxLatestOpen = brackets.pop()
                    tracker[idxLatestOpen] = s[idxLatestOpen]
                    tracker[index] = s[index]
                else:
                    tracker[index] = ""
        return "".join(tracker)
    
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = [None for _ in range(len(s))]
        parans = []
        for index, char in enumerate(s):
            if char != "(" and char != ")":
                result[index] = char
                continue

            if not parans or char == "(":
                parans.append([index, char])
                continue

            topIndex, topChar = parans[-1]
            if topChar == "(":
                parans.pop()
                result[topIndex] = topChar
                result[index] = char
            else:
                parans.append([index, char])

        resultStr = ""
        for char in result:
            if not char: continue
            resultStr += char
        return resultStr
