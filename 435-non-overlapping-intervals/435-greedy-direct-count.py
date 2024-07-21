class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], x[1]))
        right = intervals[0][1]

        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < right:
                count += 1
                right = min(right, intervals[i][1])
            else:
                right = intervals[i][1]
        return count 

# Time complexity: O(nlogn) where n is the number of intervals.
#  We use O(nlogn) time to sort the intervals.

# Space complexity: O(1) we only use a constant amount of extra space.
# The proof of the correctness of this solution can be explored if have time.