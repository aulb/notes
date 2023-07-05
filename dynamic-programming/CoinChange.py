class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # The coin amount is with DP, the coin itself is DFS
        lookup = [float('inf')] * (amount + 1)
        lookup[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                lookup[i] = min(lookup[i], 1 + lookup[i - coin])
        return -1 if lookup[amount] == float('inf') else lookup[amount]