from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_pos = 0
        next_pos = cur_pos
        
        while(cur_pos < len(nums) - 1):
            if nums[cur_pos] == 0:
                return False

            if cur_pos + nums[cur_pos] >= len(nums):
                return True

            max_pos_value = 0
            for possible_pos in range(cur_pos + 1, cur_pos + nums[cur_pos] + 1):
                pos_value = possible_pos + nums[possible_pos]
                if pos_value > max_pos_value:
                    max_pos_value = pos_value
                    next_pos = possible_pos
            
            cur_pos = next_pos

        return True


# Test cases:
# [2,3,1,1,4]
s = Solution()
print(s.canJump([3,2,1,0,4])) # True



# Comment:
# We start from the first index and keep track of the maximum position we can reach from the current position.
# We iterate through the array and update the maximum position we can reach. If the maximum position we can reach is greater than or equal to the last index, we return True. If we encounter a zero, we return False. If we reach the end of the array, we return True.