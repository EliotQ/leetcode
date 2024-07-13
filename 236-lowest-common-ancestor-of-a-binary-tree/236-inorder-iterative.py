# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

# Comment:
# If the returned value is None, it means that the node is not the ancestor of p or q.
# If the returned value is not None, it means that the node is the ancestor of p or q.
# If both left and right are not None, it means that the node is the lowest common ancestor of p and q.

# Time complexity: O(n), because we visit every node once.
# Space complexity: O(n), because we use the recursive call stack.