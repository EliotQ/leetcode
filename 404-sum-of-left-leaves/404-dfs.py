# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            left_sum = 0
            if root is None:
                return left_sum
            if root.left and not root.left.left and not root.left.right:
                left_sum += root.left.val
            else:
                left_sum += dfs(root.left)
            left_sum += dfs(root.right)
            return left_sum

        left_sum = dfs(root)
        return left_sum

# Using DFS
# Time complexity: O(N), because we visit each node exactly once.
# Space complexity: O(N), where N is the number of nodes. 
# The maximum depth of the recursion tree can be N, when the tree is skewed.