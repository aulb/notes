class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        n, m = len(num1) - 1, len(num2) - 1
        result = ''
        # Pad with 0, so its the exact same everytime
        num1 = '0' * abs(n - m) + num1 if m > n else num1
        num2 = '0' * abs(n - m) + num2 if n > m else num2

        # Iterate backwards
        for i in range(max(n, m), -1, -1):
            summed = int(num1[i]) + int(num2[i]) + carry
            result += str(summed % 10)
            carry = int(summed > 9)

        # Add the rest of the integers if any
        return ('1' if carry else '') + result[::-1]
