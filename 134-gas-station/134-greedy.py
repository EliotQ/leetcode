class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0
        total_sum = 0
        start = 0

        for i in range(0, len(cost)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        
        if total_sum < 0:
            return -1
        return start

# Comment:
# under the condition that total_sum >= 0 and there exists only one solution, 
# the start index is the only solution. (we don't need to simulate the process i.e from the start index back to the start index)
# bacause the start is the only possible solution.