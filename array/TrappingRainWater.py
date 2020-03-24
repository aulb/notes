class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        l = [0 for _ in range(length)]
        r = [0 for _ in range(length)]

        for i in range(length):
            j = length - 1 - i
            l[i] = max(height[i], l[i - 1] if i - 1 >= 0 else 0)
            r[j] = max(height[j], r[j + 1] if j + 1 < length else 0)

        trapped = 0
        for i in range(length):
            trapped += min(l[i], r[i]) - height[i]
        return trapped
