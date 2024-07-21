class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

# Comment:
# Using a greedy approach, we can solve the problem in a single pass. We keep track of the profit by adding the difference between the current and previous prices whenever the current price is greater than the previous price. We return the profit as the answer.
# Complexity Analysis
# Time complexity: O(n), where n is the length of prices.
# Space complexity: O(1).