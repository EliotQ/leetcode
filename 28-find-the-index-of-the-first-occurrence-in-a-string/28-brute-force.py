class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# Comment：
# 时间复杂度：O((m - n) * n) # m: haystack长度， n:needle长度
# 空间复杂度: O(1)