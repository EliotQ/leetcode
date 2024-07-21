class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur_money = {5:0, 10:0, 20:0}
        for i in bills:
            if i == 5:
                cur_money[5] += 1
            elif i == 10:
                if cur_money[5] > 0:
                    cur_money[5] -= 1
                    cur_money[10] += 1
                else:
                    return False
            else:
                if cur_money[5] > 0 and cur_money[10] > 0:
                    cur_money[5] -= 1
                    cur_money[10] -= 1
                    cur_money[20] += 1
                elif cur_money[5] >= 3:
                    cur_money[5] -= 3
                    cur_money[20] += 1
                else:
                    return False
        return True

# Comments:
# This solution uses a greedy algorithm to solve the problem.
# We use a dictionary to store the number of each type of bill we have.
# We iterate through the bills and update the dictionary accordingly.
# For the 20 bill, we first try to use a 10 bill and a 5 bill if possible.
# Because we want to keep the number of 5 bills as much as possible.