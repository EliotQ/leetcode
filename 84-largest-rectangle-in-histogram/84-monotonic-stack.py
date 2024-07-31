class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        
        stack = [0]
        result = 0

        for i in range(1, len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while(len(stack) > 0 and heights[i] < heights[stack[-1]]):
                    mid_index = stack[-1]
                    stack.pop()
                    if len(stack) > 0:
                        h = heights[mid_index]
                        w = i - stack[-1] - 1
                        result = max(result, h * w)
                stack.append(i)
        return result

# Comment:
# using a monotonic stack to store the index of the height in a descending order(from stack top to bottom)

# Time complexity: O(n)
# Space complexity: O(n)
