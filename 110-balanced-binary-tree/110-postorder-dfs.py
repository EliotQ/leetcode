# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if root is None:
                return 0
            left= getHeight(root.left)
            right = getHeight(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)
        return getHeight(root) != -1

# Comment:
# Time complexity: O(n)
# Space complexity: O(n)
# dfs, post-order traversal, return -1 if the tree is not balanced( height of left and right is greater than 1), otherwise return the height of the tree
# i.e. here we use one dfs to 1)calculate the height of the tree, and 2)check if the tree is balanced at the same time
# if the tree is not balanced, return -1, otherwise return the height of the tree