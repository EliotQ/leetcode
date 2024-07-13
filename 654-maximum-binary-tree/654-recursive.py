# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root_val = max(nums)
        root_idx = nums.index(root_val)
        left_nums = nums[:root_idx]
        right_nums = nums[root_idx + 1:]
        root = TreeNode(root_val)
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root

# Comment:
# Use recursive method to construct the tree, as described in the problem.
# The maximum element in the list is the root.
# The left part is the left subtree and the right part is the right subtree.
# Use recursive calls to build the tree.
# Time complexity: O(n^2) ? The index operation may take O(n) time.
# Space complexity: O(n)