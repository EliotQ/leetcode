# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        left_res = self.inorderTraversal(root.left)
        res += left_res

        res.append(root.val)

        right_res = self.inorderTraversal(root.right)
        res += right_res

        return res

# Comment：
# 时间复杂度：O(n)
# 空间复杂度：O(n)