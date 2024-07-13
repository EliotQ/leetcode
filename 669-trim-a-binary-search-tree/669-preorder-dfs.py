# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            root = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low ,high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root

# Comment:
# Using pre-order dfs to trim the binary search tree.
# Time complexity: O(n), because we visit every node once.
# Space complexity: O(n), because we use the recursive call stack.

