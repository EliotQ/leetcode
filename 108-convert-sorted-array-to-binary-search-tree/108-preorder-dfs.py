# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root_val = nums[len(nums)//2]
        root = TreeNode(val = root_val)
        left_subtree = self.sortedArrayToBST(nums[:len(nums)//2])
        right_subtree = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        root.left = left_subtree
        root.right = right_subtree
        return root

# Comment:
# Build a balanced binary search tree from a sorted array.
# Time complexity: O(n), where n is the length of the nums list.
# Space complexity: O(n), because we use the recursive call stack.