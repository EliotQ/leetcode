# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        res.append(root.val)
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        res += left + right
        return res

# Comment:
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# 递归的方法，前序遍历二叉树