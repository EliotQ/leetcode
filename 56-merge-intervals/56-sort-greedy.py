class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        ans = []

        for ele in intervals:
            if ele[0] <= right:
                right = max(right, ele[1])
            else:
                ans.append([left, right])
                left = ele[0]
                right = ele[1]
        ans.append([left, right])
        return ans

# Comment:
# Time complexity: O(nlogn)
# Space complexity: O(n)
# The sort function is O(nlogn) and the for loop is O(n)