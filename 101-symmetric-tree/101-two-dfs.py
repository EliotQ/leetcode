# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res_right_left = []
        res_left_right = []
        def mid_right_left_dfs(root):
            if root is None:
                res_right_left.append(None)
                return
            res_right_left.append(root.val)
            mid_right_left_dfs(root.right)
            mid_right_left_dfs(root.left)
        
        def mid_left_right_dfs(root):
            if root is None:
                res_left_right.append(None)
                return
            res_left_right.append(root.val)
            mid_left_right_dfs(root.left)
            mid_left_right_dfs(root.right)
        
        mid_right_left_dfs(root)
        mid_left_right_dfs(root)

        return res_right_left == res_left_right

# Time complexity: O(n)
# Space complexity: O(n)
# two dfs, one from right to left, one from left to right, compare the result of two dfs
# if they are the same, return True, otherwise False