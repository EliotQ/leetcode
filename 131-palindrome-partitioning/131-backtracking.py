class Solution:
    def is_palindrome(self, string):
        if string and string == string[::-1]:
            return True
        return False
    
    def backtracking(self, string, cur_partition, result):
        if len(string) == 0:
            result.append(cur_partition[:])
            return

        for i in range(1, len(string) + 1):
            cur_string = string[:i]
            if self.is_palindrome(cur_string):
                cur_partition.append(cur_string)
                self.backtracking(string[i:], cur_partition, result)
                cur_partition.pop()

    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, [], result)
        return result

# Time complexity: O(n * 2^n)
# Space complexity: O(n)