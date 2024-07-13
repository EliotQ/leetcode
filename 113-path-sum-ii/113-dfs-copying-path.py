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
                    ans.append(cur_path)
                return
            cur_path.append(root.val)
            dfs(root.left, targetSum - root.val, cur_path.copy())
            dfs(root.right, targetSum - root.val, cur_path.copy())
        
        ans = []
        dfs(root, targetSum, [])
        return ans

# Comment:
# Use DFS to traverse the tree and record the path.
# If the path sum is equal to the target sum, add the path to the answer.
# Time complexity: O(n) ? considering the copy operation, it may be O(n^2)
# Space complexity: O(n)

# Here we use cur_path.copy() to avoid the reference problem.
# If we use cur_path directly, the path will be changed by the next recursive call.
# So we need to copy the path to avoid this problem.
# Another way to avoid this problem is to use cur_path.pop() after the recursive call.
# See 113-dfs-pop.py for more details.
