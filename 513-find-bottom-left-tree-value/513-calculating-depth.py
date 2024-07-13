# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def find_tree_depth(root):
            if not root:
                return 0
            cur_depth = 1
            left_depth = find_tree_depth(root.left)
            right_depth = find_tree_depth(root.right)
            if left_depth > right_depth:
                cur_depth += left_depth
            else:
                cur_depth += right_depth
            return cur_depth
        
        while(root.left or root.right):
            left_subtree_depth = find_tree_depth(root.left)
            right_subtree_depth = find_tree_depth(root.right)
            if left_subtree_depth >= right_subtree_depth:
                root = root.left
            else:
                root = root.right
        
        return root.val

# Comments:
# This solution is not optimal. It calculates the depth of the tree at each step.
# It is better to use a level order traversal to find the leftmost element in the last level of the tree.

# Time complexity is not O(n), it is O(n^2) because we are calculating the depth of the tree at each step.
# Space complexity is O(n) because of the recursion stack.
