class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        left = 0
        right = k

        while(left < len(s)):
            if right > len(s):
                right = len(s)
            
            p_1 = left
            p_2 = right - 1
            while(p_1 < p_2):
                temp = s[p_1]
                s[p_1] = s[p_2]
                s[p_2] = temp
                p_1 += 1
                p_2 -= 1
            
            left += 2 * k
            right += 2 * k

        return ''.join(s)

# Comment:
# 时间复杂度：O(n)
# 空间复杂度：O(1)