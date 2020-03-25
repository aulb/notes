class Solution:
    phoneNum = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": " ",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        if len(digits) == 1: return self.phoneNum[digits]
        toReturn = []
        digit = digits[0]
        for char in self.phoneNum[digit]:
            for extend in self.letterCombinations(digits[1:]):
                toReturn.append(char + extend)
        return toReturn
