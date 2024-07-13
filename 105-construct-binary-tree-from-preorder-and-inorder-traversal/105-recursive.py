# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_idx = inorder.index(preorder[0])

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]

        left_preorder = preorder[1:root_idx + 1]
        right_preorder = preorder[root_idx + 1:]
        
        root = TreeNode(val = preorder[0])
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root

# Comment:
# Use recursive method to construct the tree.
# The first element in preorder list is the root.

# A key condition is "preorder and inorder consist of unique values."