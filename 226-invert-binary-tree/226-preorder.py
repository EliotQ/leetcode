# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp
        return root

# Comment:
# Time complexity: O(n). Since each node is visited once, the time complexity is O(n).
# Space complexity: O(n), where n is the number of nodes in the tree. The number of recursive calls is bound by the height of the tree.