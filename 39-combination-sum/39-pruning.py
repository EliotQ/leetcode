class Solution:
    def backtracking(self, candidates, target, start_index, path, result):
        if sum(path) == target:
            result.append(path[:])
            return

        for i in range(start_index, len(candidates)):
            if sum(path) + candidates[i] > target:
                break
            path.append(candidates[i])
            self.backtracking(candidates, target,  i, path, result)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtracking(candidates, target, 0, [], result)
        return result

# Time complexity: O(n^target), because we have n choices for each target.
# Space complexity: O(n^target), consider the worst case where the recursion goes n levels deep each time.