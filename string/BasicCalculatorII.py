class Solution:
    def calculate(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        prev = "+"
        strs = iter(list(s + "+"))
        vals = [0]
        number = 0
        for c in strs:
            if c == " ": continue
            if c.isdigit(): number = number * 10 + int(c)
            else:
                if prev == "*": vals[-1] *= number
                if prev == "/":
                    vals[-1] /= number
                    if vals[-1] < 0: vals[-1] = math.ceil(vals[-1])
                    else: vals[-1] = math.floor(vals[-1])
                if prev == "+":
                    vals.append(number)
                if prev == "-":
                    vals.append(-number)
                prev = c
                number = 0

        return sum(vals)
