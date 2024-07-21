class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[0],x[1]))
        left, right = points[0][0], points[0][1]

        count = 1
        for i in range(len(points)):
            if points[i][0] > right:
                count += 1
                left = points[i][0]
                right = points[i][1]
            else:
                left = max(left, points[i][0])
                right = min(right, points[i][1])
        return count

# In this solution, we first sort the points by their start position, 
# when the start position is the same, we sort them by their end position. (this is not necessary, but it makes the code more readable)
# Then we iterate through the points, and update the left and right boundary of the current arrow.
# If the current point is not covered by the current arrow, we need a new arrow, and update the left and right boundary.
# If the current point is covered by the current arrow, we update the left and right boundary accordingly.
# Finally, we return the number of arrows needed.

# The correctness of this solution can be proved by induction.

# Time complexity: O(nlogn) where n is the number of points. We use O(nlogn) time to sort the points.
# Space complexity: O(1) we only use a constant amount of extra space.