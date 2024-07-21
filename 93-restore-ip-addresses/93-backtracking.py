class Solution:
    def is_valid(self, string):
        if string:
            if string[0] == '0':
                if len(string) == 1:
                    return True
            elif 0 <= int(string) <= 255:
                return True
        return False
    
    def backtracking(self, s, start_index, target, path, result):
        if target == 0 and len(s) == 0:
            result.append('.'.join(path))
            return
        for i in range(1, len(s) + 1 - (target - 1)):
            if self.is_valid(s[:i]):
                path.append(s[:i])
                self.backtracking(s[i:], i + 1, target - 1, path, result)
                path.pop()
            else:
                return
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        target = 4
        result = []
        self.backtracking(s, 0, target, [], result)
        return result

# Comment:
# The relationship between backtracking and DFS is that backtracking is a specific form of DFS.

# We can do pruning in the backtracking process to reduce the number of unnecessary recursive calls.
# Leave for later.