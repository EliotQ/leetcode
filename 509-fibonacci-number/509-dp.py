class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

# Comment:
# Here we omit the dp array and only keep the last two numbers, because we only need the last two numbers to calculate the next number.
# Time complexity: O(n)
# Space complexity: O(1)