class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        maxSoFar = 0
        l = 0
        r = len(height) - 1

        while r > l:
            maxSoFar = max(maxSoFar, (r - l) * min(height[r], height[l]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxSoFar
