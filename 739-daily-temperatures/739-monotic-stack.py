class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculates the number of days you would have to wait until a warmer temperature for each day.

        Args:
            temperatures (List[int]): A list of daily temperatures.

        Returns:
            List[int]: A list of integers representing the number of days you would have to wait until a warmer temperature for each day.
        """
        if len(temperatures) <= 1:
            return [0]
        result = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0  and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return result

# Comment:
# This solution uses a monotonic stack to calculate the number of days you would have to wait until a warmer temperature for each day.
# It iterates through the temperatures and maintains a stack of indices of temperatures that are yet to find a warmer temperature.
# If a temperature is lower than or equal to the temperature at the top of the stack, it is added to the stack.
# If a temperature is higher than the temperature at the top of the stack, it means a warmer temperature has been found.
# In this case, the function pops temperatures from the stack and calculates the number of days until a warmer temperature for each popped temperature.
# The result is stored in the result list at the corresponding index.
# Finally, the result list is returned.

# Time complexity: O(n)
# Space complexity: O(n)