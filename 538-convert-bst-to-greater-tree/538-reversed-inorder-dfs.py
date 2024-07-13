# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reversed_inorder_dfs(node, cur_sum):
            if not node:
                return cur_sum
            if node and not node.right:
                node.val += cur_sum
                cur_sum = reversed_inorder_dfs(node.left, node.val)
                return cur_sum
            
            cur_sum = reversed_inorder_dfs(node.right, cur_sum)
            node.val += cur_sum
            cur_sum = reversed_inorder_dfs(node.left, node.val)
            return cur_sum

        reversed_inorder_dfs(root, 0)
        return root

# Time complexity: O(n), where n is the number of nodes in the binary search tree.
# Space complexity: O(h), where h is the height of the binary search tree.

# A more concise version of the above solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reversed_inorder_dfs(node, cur_sum):
            if not node:
                return cur_sum

            if node.right:
                cur_sum = reversed_inorder_dfs(node.right, cur_sum)
            node.val += cur_sum
            cur_sum = reversed_inorder_dfs(node.left, node.val)
            return cur_sum

        reversed_inorder_dfs(root, 0)
        return root

# Here we remove the redundant base case check for the right child of the node.
# However, if we want to remove the base case check for the left child of the node,
# we need to modify the code as follows:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reversed_inorder_dfs(node, cur_sum):
            if not node:
                return cur_sum

            if node.right:
                cur_sum = reversed_inorder_dfs(node.right, cur_sum)

            node.val += cur_sum
            cur_sum = node.val
            
            if node.left:
                cur_sum = reversed_inorder_dfs(node.left, cur_sum)
            return cur_sum

        reversed_inorder_dfs(root, 0)
        return root

# here we cannot write as:

#            node.val += cur_sum
#            
#            if node.left:
#                cur_sum = reversed_inorder_dfs(node.left, node.val)
#            return cur_sum

# The reason is that when node.val is passed into the recursive call of reversed_inorder_dfs,
# its value is changed in the recursive call, which will affect the value of node.val in the current call.