class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ele in s:
            if len(stack) == 0 or stack[-1] != ele:
                stack.append(ele)
            else:
                stack.pop()
        return ''.join(stack)

# Commnet:
# 用栈存储尚未匹配的元素，若栈顶元素与新元素匹配则弹栈，否则压栈
# 时间复杂度：O(n)
# 空间复杂度：O(n)