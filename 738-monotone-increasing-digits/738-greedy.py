class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        string = str(n)
        for i in range(len(string) - 1, 0, -1):
            if int(string[i-1]) > int(string[i]):
                string = string[:i-1] + str(int(string[i-1]) - 1) + '9' * len(string[i:])
        return int(string)

# Comment:
# Here we are using a greedy approach to solve the problem.
# We iterate through the string from right to left and check if the current digit is greater than the next digit(left digit).
# If it is, we decrement the current digit by 1 and set all the digits to the right of it to 9.
# Example: 98

# Time complexity: O(n)
# Space complexity: O(n)
