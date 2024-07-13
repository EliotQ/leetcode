# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, targetSum, cur_path):
            if not root:
                return
            if root and not root.left and not root.right:
                if root.val == targetSum:
                    cur_path.append(root.val)
                    ans.append(cur_path[:])
                    cur_path.pop()
                return
            cur_path.append(root.val)
            dfs(root.left, targetSum - root.val, cur_path)
            dfs(root.right, targetSum - root.val, cur_path)
            cur_path.pop()
        
        ans = []
        dfs(root, targetSum, [])
        return ans

# Comment:
# This way we can keep the path unchanged.
# One thing to note is that when we append the path to the answer, we need to use cur_path[:] to make a copy of the path.
# Otherwise, the path will be changed by the next recursive call.

    