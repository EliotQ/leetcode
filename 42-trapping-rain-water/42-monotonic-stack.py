class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        stack = [0]
        result = 0

        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while(len(stack) > 0 and height[i] > height[stack[-1]]):
                    mid_height = height[stack[-1]]
                    stack.pop()
                    if stack:
                        left_height = height[stack[-1]]
                        right_height = height[i]
                        h = min(left_height, right_height) - mid_height
                        w = i - stack[-1] - 1
                        result += h * w
                stack.append(i)
        return result

# Comment:
# using a monotonic stack to store the index of the height in a ascending order(from stack top to bottom)
# then calculate the water that can be trapped at the current index if the current height is greater than the height of the top of the stack

# Time complexity: O(n)
# Space complexity: O(n)
