from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(0, len(gas)):
            cur_pos = start
            cur_gas = gas[start]
            # ascending
            while(cur_gas >= cost[cur_pos]):
                cur_gas -= cost[cur_pos]
                cur_pos = (cur_pos + 1) % len(gas)
                cur_gas += gas[cur_pos]
                if cur_pos == start:
                    return start
        return -1

# Test cases:
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
s = Solution()
print(s.canCompleteCircuit(gas, cost)) # expect 4