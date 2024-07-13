# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_dfs(root):
            res = []
            if not root:
                return []
            res += inorder_dfs(root.left)
            res.append(root.val)
            res += inorder_dfs(root.right)
            return res
        
        ans = inorder_dfs(root)
        return all(ans[i] < ans[i+1] for i in range(len(ans)-1))

# Time complexity: O(n)
# Space complexity: O(n), for the inorder traversal list
# The inorder traversal of a binary search tree is sorted in strictly ascending order.
# We can check if the inorder traversal is sorted.
