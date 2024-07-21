class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path) - 1) + 1 ):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()

# Comment:
# In cuttting branches, we can use n - (k - len(path) - 1) + 1 to reduce the number of branches.
# The reason is that , we need to choose (k - len(path)) staring from the startIndex,
# so the remaining elements should be greater than or equal to k - len(path).
# That means, from X to n (both including), there should be exactly k - len(path) elements.
# So, the X is n - (k - len(path) - 1),
# and we have a + 1 to include the last element.
# and the range should be from startIndex to n - (k - len(path) - 1) + 1.

# Time complexity: O(C(n, k) * k)
# Space complexity: O(C(n, k) * k)