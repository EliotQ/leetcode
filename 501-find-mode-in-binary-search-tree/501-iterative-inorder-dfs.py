# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        node = root
        stack = []
        traversal = []

        while(node or stack):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node.val)
                node = node.right
        count_dict = {k:traversal.count(k) for k in set(traversal)}
        ans = [k for k in set(traversal) if count_dict[k] == max(count_dict.values())]
        return ans

# Comment:
# Time complexity: O(n), because we visit every node once.
# Space complexity: O(n), because we store all the nodes in the list.
# The space complexity can be improved to O(1) if we store the last value and the maximum count.
# also, we may not need to use the dictionary to count the frequency of each value, because it's already a increasing order list.
# Leave this for now, and come back later to improve !)the space complexity and 2)the way to find the mode.