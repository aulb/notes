class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        if not num: return True

        l, r = 1, num
        while r >= l:
            m = l + (r - l) // 2
            if m == num / m: return True
            if m > num / m:
                r = m - 1
            else:
                l = m + 1
        return False
