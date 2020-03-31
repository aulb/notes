class Solution:
    def maximum69Number (self, num: int) -> int:
        numArr = list(str(num))
        for i, num in enumerate(numArr):
            if num != "9":
                numArr[i] = "9"
                break
        return int("".join(numArr))
