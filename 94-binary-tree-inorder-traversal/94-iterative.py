# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        traversal = []
        node = root
        stack = []

        while(node or stack):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node.val)
                node = node.right
        return traversal

# Comment:
# Time complexity: O(n), because we visit every node once.
# Space complexity: O(n), because we store all the nodes in the list.
# This is the iterative inorder traversal of a binary tree.
