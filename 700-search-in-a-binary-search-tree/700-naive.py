# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        cur_val = root.val
        if cur_val == val:
            return root
        elif cur_val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Time complexity: O(n)
# For the worst case, we need to visit all the nodes.
# Space complexity: O(n)
# For the worst case, the depth of the recursion is n.

# The above solution is a recursive solution, follow the instruction of the problem, and leverage the property/definition of the binary search tree.