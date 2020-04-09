class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        curr = 0 # red, white = 1, blue = 2
        while slow < len(nums):
            for fast in range(slow, len(nums)):
                if nums[fast] == curr:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
            curr += 1
## Dutch National Flag
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         red, white, blue = 0, 0, len(nums)-1
#         while white <= blue:
#             if nums[white] == 0:
#                 nums[red], nums[white] = nums[white], nums[red]
#                 white += 1
#                 red += 1
#             elif nums[white] == 1:
#                 white += 1
#             else:
#                 nums[white], nums[blue] = nums[blue], nums[white]
#                 blue -= 1
