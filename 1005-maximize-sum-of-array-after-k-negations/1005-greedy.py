from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        count_negative = 0
        for i in nums:
            if i < 0:
                count_negative += 1
        if k >= count_negative:
            if (k - count_negative) % 2 == 0:
                result = sum([abs(i) for i in nums])
                return result
            else:
                result = sum([abs(i) for i in nums]) - 2 * min([abs(i) for i in nums])
                return result
        
        elif k < count_negative:
            result = sum([i for i in nums if i > 0]) + 2 * sum(sorted([-i for i in nums if i < 0])[-k:]) + sum(sorted([i for i in nums if i < 0]))
            return result

# Test cases:
nums = [2,-3,-1,5,-4]
k = 2
s = Solution()
print(s.largestSumAfterKNegations(nums, k)) # 13

# Comment:
# We count the number of negative numbers in the array. 
# If the number of negative numbers is greater than or equal to k, we negate all the negative numbers in the array. 
# And if the difference between k and the number of negative numbers is even, we return the sum of the array after negating the numbers. 
# If the difference between k and the number of negative numbers is odd, we negate the minimum number in the array and return the sum of the array after negating the numbers.

# If the number of negative numbers is less than k, we negate the minimum k negative numbers in the array. We return the sum of the array after negating the numbers.