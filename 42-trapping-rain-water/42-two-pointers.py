class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max = [0] * len(height)
        post_max = [0] * len(height)
        result = 0

        for i in range(1, len(height)):
            pre_max[i] = max(pre_max[i-1], height[i-1])
        
        for i in range(len(height)-2, 0, -1):
            post_max[i] = max(post_max[i+1], height[i+1])
        
        for i in range(1, len(height) - 1):
            result += max(min(pre_max[i], post_max[i]) - height[i], 0)
        
        return result

# Comment:
# using two pointers to store the max height of the left and right side of the current index
# then calculate the water that can be trapped at the current index
# Time complexity: O(n)
# Space complexity: O(n)