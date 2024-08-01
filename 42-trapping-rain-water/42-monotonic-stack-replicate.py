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
                while(stack and height[i] > height[stack[-1]]):
                    mid_index = stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        h = min(height[left_index], height[right_index]) - height[mid_index]
                        w = right_index - left_index - 1
                        result += h * w
                stack.append(i)
        return result