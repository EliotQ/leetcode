# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder_dfs(root):
            if not root:
                return []
            res = []
            res += inorder_dfs(root.left)
            res.append(root.val)
            res += inorder_dfs(root.right)
            return res
        res = inorder_dfs(root)
        return min([abs(res[i+1] - res[i]) for i in range(len(res) - 1)])

#  Comment:
#  Time complexity: O(n), because we visit every node once.
#  Space complexity: O(n), because we store all the nodes in the list.
#  The space complexity can be improved to O(1) by using the iterative inorder traversal.
#  The time complexity is still O(n) because we visit every node once.
#  Also, we can use two pointers to keep track of the last value and the minimum difference.