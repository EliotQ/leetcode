class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        for j in range(1, len(s)+1):
            for i in wordDict:
                if (j >= len(i)) and (dp[j-len(i)]== True) and (s[j-len(i):j] == i) :
                    dp[j] = True
        return dp[len(s)]

# Comment:
# This problem is permutation with repetition.
# We first iterate over the knapsack capacity, then the items.

# Time complexity: O(n*m), where n is the length of the string, and m is the length of the wordDict.
