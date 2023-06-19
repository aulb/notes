from collections import Counter
# This solution is for when the str can be anything, ran into time limit error
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: return []
        result = [[strs[0]]]
        resultCounters = {0: Counter(strs[0])}
        
        for index in range(1, len(strs)):
            currentStr = strs[index]
            currentStrCounter = Counter(currentStr)
            matchIndex = self.compareToResult(resultCounters, currentStrCounter)
            if matchIndex != -1: result[matchIndex].append(currentStr)
            else: 
                result.append([currentStr])
                resultCounters[len(result) - 1] = currentStrCounter
        return result
    
    def compareToResult(self, resultCounters, currentCounter):
        for index in list(resultCounters.keys()):
            if resultCounters[index] == currentCounter: return index
        return -1
    
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            key = self.getKey(string)
            groupedAnagram = result.get(key, None)
            if groupedAnagram is None:
                result[key] = [string]
            else:
                groupedAnagram.append(string)
        return result.values()

    def getKey(self, string):
        key = [0] * 26
        for char in string:
            key[ord(char) - 97] += 1
        return ','.join([str(num) for num in key])