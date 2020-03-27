class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return x

        l, r = 1, x
        while r >= l:
            m = l + (r - l) // 2
            if m == x / m: return m
            if m > x / m:
                r = m - 1
            else:
                l = m + 1
        return r # r was the closest match before l overtakes
