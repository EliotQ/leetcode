# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif not root.left or not root.right:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while(successor.left):
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            root = successor
        return root·

# Comment:
# Time complexity: O(H) where H is the height of the tree
# Space complexity: O(H) where H is the height of the tree
# This is the recursive solution to delete a node in a binary search tree.
# The key idea when the root value is equal to the key is to find the inorder successor of the root node.
# The inorder successor is the leftmost node in the right subtree of the root node.
