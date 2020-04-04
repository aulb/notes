class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b: return a or b
        if len(b) > len(a): a, b = b, a
        return self.addBinaryHelper(a, b)

    def addBinaryHelper(self, a:str, b:str) -> str:
        carry = 0
        result = [char for char in a]
        aP = len(a) - 1 # aPointer
        for bP in range(len(b) - 1, -1, -1): # bPointer
            nextCarry = 1 if int(b[bP]) + int(a[aP]) + carry > 1 else 0
            result[aP] = str(int(b[bP]) ^ int(a[aP]) ^ carry)
            carry = nextCarry
            aP -= 1

        # aRemainder
        for aR in range(aP, -1, -1):
            if not carry: break
            nextCarry = 1 if int(a[aR]) + carry > 1 else 0
            result[aR] = str(int(a[aR]) ^ carry)
            carry = nextCarry

        if carry: return "1" + "".join(result)
        return "".join(result)
