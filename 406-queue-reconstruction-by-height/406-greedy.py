class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []

        for p in people:
            queue.insert(p[1], p)
        return queue

# Comment:
# In this solution, we first sort the people by their height in descending order, 
# when the height is the same, we sort them by their k value in ascending order.

# Then we iterate through the sorted people list, and insert each person into the queue at the k-th position.
# Because the people with higher height are already in the queue, the k value of the current person is the number of people in front of him,
# so we can insert him at the k-th position directly.
# After inserting all the people, we get the final queue.

# It can be proved that the final queue is the correct answer by induction.
# ? If have time, try to prove it.