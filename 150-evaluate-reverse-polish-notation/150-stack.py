class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele in '+-*/':
                op2 = stack.pop()
                op1 = stack.pop()
                if ele == '+':
                    res = int(op1) + int(op2)
                    stack.append(res)
                elif ele == '-':
                    res = int(op1) - int(op2)
                    stack.append(res)
                elif ele == '*':
                    res = int(op1) * int(op2)
                    stack.append(res)
                else:
                    res = int(int(op1) / int(op2))
                    stack.append(res)
            else:
                stack.append(ele)
        return int(stack.pop())

# Comment:
# 时间复杂度：O(n)
# 空间复杂度：O(n)