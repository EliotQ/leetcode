class Solution:
    def backtracking(self, cur, n, digits, result):
        num2char = {
        '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz' 
        }

        if len(cur) == n:
            result.append(cur[:])
            return
        
        for char in num2char[digits[0]]:
            cur = cur + char
            self.backtracking(cur, n, digits[1:], result)
            cur = cur[:-1]
        

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        n = len(digits)
        result = []
        self.backtracking('', n, digits, result)
        return result

# Time complexity: O(4^n)
# because each digit has at most 4 characters.
# Space complexity: O(4^n)