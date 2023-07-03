class Solution:
    digits_to_letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit = digits[0]
        digitLetters = self.digits_to_letters[digit]
        if len(digits) == 1: return digitLetters
        currentResult = []
        stringCombo = self.letterCombinations(digits[1:])
        for letter in digitLetters:
            for string in stringCombo:
                currentResult.append(f'{letter}{string}')
        return currentResult