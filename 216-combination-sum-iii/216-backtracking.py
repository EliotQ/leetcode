class Solution:
    def backtracking(self, k, n, startIndex, cur, result):
        if sum(cur) == n and len(cur) == k:
            result.append(cur[:])
            return 
        if (sum(cur) > n) or (len(cur) > k):
            return
        
        for i in range(startIndex, 9 - (k - len(cur) - 1) + 1):
            cur.append(i)
            self.backtracking(k , n, i + 1, cur, result)
            cur.pop()
            
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(k, n, 1, [], result)
        return result

# Time complexity: O(C(9, k) * k)
# the * k is because we need to copy the list to the result.
# Space complexity: O(C(9, k) * k)