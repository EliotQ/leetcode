from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        for i, ch in enumerate(s):
            last_seen[ch] = i

        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last_seen[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result


# Time complexity: O(n) where n is the length of the input string s.
#  We iterate through the string twice, and each iteration takes O(n) time.
# Space complexity: O(1) we use a constant amount of extra space.

# The correctness of this solution can be proved by induction. If have time.

# The solution below is wrong:

# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         last_seen = {}
#         for i, ch in enumerate(s):
#             last_seen[ch] = i

#         result = []
#         start = 0
#         for i, ch in enumerate(s):
#             end = last_seen[ch]
#             if i == end:
#                 result.append(last_seen[ch] - start + 1)
#                 start = i + 1
#         return result

# Because the end variable is not updated correctly, the solution above is wrong.
# The end variable should be updated by max(end, last_seen[ch]) instead of last_seen[ch].
# The reason is that we need to find the last position of the character in the current partition,
# so we should update the end variable by the maximum of the current end and the last position of the character.
# That's to say, it's not enough to update the end variable by the last position of the character,
# we should update it by the maximum of the current end and the last position of the character.
# the end serves the current partition, but the last_seen[ch] only serves the character.

# An example that fails the solution above is "abac", where the correct answer is [3, 1], but the solution above returns [2, 1, 1]
# because the end variable is not updated correctly.

# Test cases:
# "abac" => [3, 1]
s = Solution()
print(s.partitionLabels("abac"))

