# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root):
        if not root:
            return [0, 0]
        left = self.traversal(root.left)
        right = self.traversal(root.right)

        # rob current
        val_rob_current = root.val + left[1] + right[1]

        # not rob current
        val_not_rob_current = max(left[0], left[1]) + max(right[0], right[1])

        return [val_rob_current, val_not_rob_current]

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)

# Comment:
# We define the dp array as [val_rob_current, val_not_rob_current].
# The transition function is:
# 1. if we rob the current house, then we can't rob the children of the current house, 
#    so the money we get is root.val + left[1] + right[1]
# 2. if we don't rob the current house, then we can rob the children of the current house or not,
#    so the money we get is max(left[0], left[1]) + max(right[0], right[1])

# Time complexity: O(n), because we traverse the tree once.
# Space complexity: O(n), because we use the recursion stack.

