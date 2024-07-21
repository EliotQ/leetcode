class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        right = intervals[0][1]

        count = 1 # counts of overlapping intervals

        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                count += 1
                right = intervals[i][1]
            else:
                right = min(right, intervals[i][1])
        return len(intervals) - count