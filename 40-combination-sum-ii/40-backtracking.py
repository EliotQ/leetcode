class Solution:
    def backtracking(self, candidates, target, start_index, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        for i in range(start_index, len(candidates)):
            if sum(path) + candidates[i] > target:
                break
            
            if i > start_index and candidates[i - 1] == candidates[i]:
                continue
            
            path.append(candidates[i])
            self.backtracking(candidates, target, i + 1, path, result)
            path.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtracking(candidates, target, 0, [], result)
        return result