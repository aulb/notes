class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Its a simple-ish question, don't overthink
        # You were right about just finding three distinct numbers
        # Solution is to just find 3 lowest numbers
        # [10,9,1,2,0,3]
        # [1,1,1,1,1,1]
        first = second = float("inf")
        for num in nums:
            if first >= num: first = num # >= make sure same cases are counted
            elif second >= num: second = num
            else: return True
        return False
