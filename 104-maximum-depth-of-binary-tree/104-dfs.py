# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# Comment：
# finding the depth using dfs, post-order traversal. 
# The post-order traversal actually calculates the height of the root node, and the height of the root node is the maximum depth of the tree.
# i.e. we calculate the height of the root to get the maximum depth of the tree.
# time complexity: O(n)
# space complexity: O(n)