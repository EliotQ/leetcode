# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right

        left_depth = 0 
        while(left):
            left = left.left
            left_depth += 1

        right_depth = 0
        while(right):
            right = right.right
            right_depth += 1
        
        if left_depth == right_depth:
            tree_depth = left_depth + 1
            return 2 ** tree_depth - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# Using DFS, when the subtree is a complete tree, we can calculate the number of nodes directly.
# Time complexity is not determined and need further investigation.