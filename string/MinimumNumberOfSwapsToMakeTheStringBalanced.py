class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        maximumImbalance = 0
        for char in s:
            if char == "[":
                imbalance -= 1
            else:
                imbalance += 1
            maximumImbalance = max(maximumImbalance, imbalance)
        return (maximumImbalance + 1) // 2