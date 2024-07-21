class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_pos = 0
        step_count = 0

        while(cur_pos < len(nums) - 1):
            if cur_pos + nums[cur_pos] >= len(nums) - 1:
                step_count += 1
                return step_count

            max_pos_value = 0
            for possible_pos in range(cur_pos + 1, cur_pos + nums[cur_pos] + 1):
                pos_value = possible_pos + nums[possible_pos]
                if pos_value > max_pos_value:
                    max_pos_value = pos_value
                    next_pos = possible_pos
            
            cur_pos = next_pos
            step_count += 1
        
        return step_count

# Comment:
# Using the same logic as the snippet from 55-jump-game/55-greedy.py, we can solve this problem by keeping track of the maximum position we can reach from the current position. We iterate through the array and update the maximum position we can reach. If the maximum position we can reach is greater than or equal to the last index, we return the number of steps taken. If we encounter a zero, we return the number of steps taken. If we reach the end of the array, we return the number of steps taken.
# Time complexity: O(n^2), because we iterate through the array and update the maximum position we can reach for each element in the array.
# ? Need further verification on the time complexity.