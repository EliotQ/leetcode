n, v = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(v+1)
for i in range(n):
    for j in range(weight[i][0], v+1):
        dp[j] = max(dp[j], dp[j-weight[i][0]] + weight[i][1])
print(dp[v])

# Comment:
# Using dynamic programming to solve this problem.
# Time complexity: O(n*v), where n is the number of items and v is the maximum volume.
# Space complexity: O(v), where v is the maximum volume.

# Complete knapsack problem.
# Here we iterate the j from left to right, because we are allowed to use the same item multiple times.
