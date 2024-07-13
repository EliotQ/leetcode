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
        if min(p.val, q.val) < root.val < max(p.val, q.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: # p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

# Comment:
# Given the binary search tree property, we can determine the subtree that contains the lowest common ancestor, by comparing the values of the nodes.

# Time complexity: O(n), because we visit every node once.
# Space complexity: O(n), because we use the recursive call stack.