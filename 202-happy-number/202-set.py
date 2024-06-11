class Solution:
    def isHappy(self, n: int) -> bool:
        number_set = set()
        
        while(True):
            n = str(n)
            new_number = 0
            for i in n:
                new_number += int(i) ** 2
            print(new_number)
            if new_number in number_set:
                return False
            elif new_number == 1:
                return True
            else:
                number_set.add(new_number)
                n = new_number

# Comment:
# 用set保存已经出现过的数字