class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        max_distance = nums[0]
        step_counter = 1
        current_max_distance = max_distance # zone
        for index in range(1, len(nums)):
            if current_max_distance >= len(nums) - 1:
                return step_counter  
            num = nums[index]
            max_distance = max(index + num, max_distance)
            if index >= current_max_distance:
                # go to a new "zone"
                current_max_distance = max_distance
                step_counter += 1           
        return step_counter

# [8,2,6,4,0,0,1,1,1,6,5,1,7,0,3,8,1,8,0,9,4,2,8,2,0,1,2,3,3,4,2,1,6,8,7,9,8,9,0,1,7,7,3,4,0,6,2,1,6,5,0,0,9,0,4,0,1,9,5,4,3,7,8,9,6,7,8]

# [0]
# [1,2]

# [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3,1] # 7 --> 7 --> 3
#    0,9,6,9,6,1,7 # => everytime we create new "zone" we increment step by 1
#                  9,0,1,2,9,0,3

    def jump_with_recursion(self, nums: List[int]) -> int:
        # Get min jump from k, end
        # end = len(nums) - 1
        # start = 0
        # [2,3,0,1,4]
        # 2 [0, 4] => 3 [1, 4] => 1 [3, 4] => 4 [4, 4] # 4 jumps needed
        #                      => 4 [4, 4] # 3 jumps needed
        # Skip if num at index is 0
        if not nums or nums[0] == 0: return 0
        return self.helper(nums, 0)[1]

    def helper(self, nums: List[int], start: int) -> Tuple[bool, int]: 
        # Can make it to the end, steps to the end
        # Arrive at the end already, return immediately
        if start == len(nums) - 1: return (True, 0)

        how_far_can_jump = nums[start]
        if how_far_can_jump == 0: return (False, -1)

        result = []
        for distance in range(how_far_can_jump):
            new_start = start + distance + 1
            if new_start < len(nums):
                result.append(self.helper(nums, new_start))
        result = [steps[1] for steps in filter(lambda x: x[0], result)]
        if not result: return (False, -1)
        return (True, 1 + min(result))

