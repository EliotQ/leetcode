# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        number = 0
        if not root:
            return number
        number += 1
        number += self.countNodes(root.left)
        number += self.countNodes(root.right)
        return number

# Using DFS
# Time complexity: O(N), because we visit each node exactly once.
# Space complexity: O(N), where N is the number of nodes.
# The maximum depth of the recursion tree can be N, when the tree is skewed.