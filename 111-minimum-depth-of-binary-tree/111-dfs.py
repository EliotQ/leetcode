# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left, right) + 1

# Comment:
# The trick here compared to the maxDepth is that, when one side is empty (depth = 0), we should return the depth of the other side + 1, instead of 0,
# because the empty side should not be counted as a leaf node.
# time complexity: O(n), because we need to traverse all nodes 
# space complexity: O(n), because of the recursion stack, in the worst case, the recursion stack will be as deep as the height of the tree