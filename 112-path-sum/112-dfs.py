# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if root and not root.left and not root.right:
            return root.val == targetSum
        
        left_res = self.hasPathSum(root.left, targetSum - root.val)
        if left_res:
            return True
        
        right_res = self.hasPathSum(root.right, targetSum - root.val)
        if right_res:
            return True
        
        return False

# Comment:
# This solution uses a depth-first search (DFS) approach to check if there is a path from the root to a leaf node
# that sums up to the target sum.
# At each node, we subtract the node's value from the target sum and recursively check if the left or right subtree
# has a path that sums up to the remaining target sum.
# If the current node is a leaf node and its value is equal to the remaining target sum, we return True，otherwise False.
# The method to check if a node is a leaf node is to check if it is not none an has no left and right children.

# If either subtree has such a path, we return True.
# If neither subtree has such a path, we return False.
# The time complexity of this solution is O(n), where n is the number of nodes in the tree.
# The space complexity is also O(n) due to the recursion stack.