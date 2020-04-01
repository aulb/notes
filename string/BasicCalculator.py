class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Think about it as number sign number sign
        strs = iter(list(s + "+"))
        add, sub = "+", "-"
        signs = { add: 1, sub: -1 }
        def getIntermediateResult():
            sumSoFar = 0
            digit = 0
            prev = add
            for c in strs:
                if c == " ": continue
                if c.isdigit(): digit = digit * 10 + int(c)
                if c == add or c == sub:
                    digit *= signs[prev]
                    sumSoFar += digit
                    prev = c
                    digit = 0
                if c == "(":
                    sumSoFar += signs[prev] * getIntermediateResult()
                if c == ")":
                    sumSoFar += signs[prev] * digit
                    return sumSoFar
            return sumSoFar
        return getIntermediateResult()

# "(1-((4+5)-2)-3)+(6+8)" => 1-4-5+2-3+6+8
# ( - prev is +
# ( - prev is -, until we find ), all calculations are reverted
