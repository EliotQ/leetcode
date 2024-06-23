class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', ']':'[', '}':'{'}
        for ele in s:
            if len(stack) == 0 or ele in '([{':
                stack.append(ele)
            elif stack[-1] != pair[ele]:
                stack.append(ele)
            else:
                stack.pop()
        return len(stack) == 0

# Comment:
# 用栈存储尚未匹配的元素，若栈顶元素与新元素匹配则弹栈，否则压栈
# 时间复杂度：O(n)
# 空间复杂度：O(n)