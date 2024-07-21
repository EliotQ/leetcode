class Solution:
    def backtracking(self, candidates, target, start_index, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        if sum(path) > target:
            return
        for i in range(start_index, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target,  i, path, result)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, target, 0, [], result)
        return result

# Time complexity: O(n^target), because we have n choices for each target.
# Space complexity: O(n^target), consider the worst case where the recursion goes n levels deep each time.
# ? This needs to be verified.

# A better pruning strategy is to sort the candidates array first, and then we can stop the search when the sum of the path exceeds the target.
# see 39-combination-sum/39-pruning.py for the pruning strategy.

