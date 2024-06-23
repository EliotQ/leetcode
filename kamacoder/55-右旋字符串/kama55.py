k = int(input())
s = input()

n = len(s)
k = k % n

s_new = ''
s_new += s[n-k:n]
s_new += s[0:n-k]
print(s_new)


# Comment:
# 时间复杂度：O(n)
# 空间复杂度：O(n)