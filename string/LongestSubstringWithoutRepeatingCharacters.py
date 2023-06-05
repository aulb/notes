class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        # When we see duplicate character, we need to advance the start of the substring
        # to the index + 1 of the duplicate character's last index prior
        # abca -> start = 0 ==> start = 1, before was abc ==> bca
        usedCharIndices = {} # keeps track of the latest index of the char
        maxLength = startIndexOfSubstring = 0
        for index, char in enumerate(string):
            if char in usedCharIndices and usedCharIndices[char] >= startIndexOfSubstring:
                startIndexOfSubstring = usedCharIndices[char] + 1
            maxLength = max(maxLength, index - startIndexOfSubstring + 1)
            usedCharIndices[char] = index
        return maxLength 