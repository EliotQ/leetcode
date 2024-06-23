s = input()
s_new = ''
 
for char in s:
    if char in '0123456789':
        s_new += 'number'
    else:
        s_new += char
 
print(s_new)

# Comment: 
# 时间复杂度：O(n)
# 空间复杂度：O(n)