# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1, root2):
            if root1 and root2:
                root3 = TreeNode(val = root1.val + root2.val)
                root3.left = dfs(root1.left, root2.left)
                root3.right = dfs(root1.right, root2.right)
            elif not root1 and not root2:
                return None
            elif root1 and not root2:
                root3 = TreeNode(val = root1.val)
                root3.left = dfs(root1.left, None)
                root3.right = dfs(root1.right, None)
            elif root2 and not root1:
                root3 = TreeNode(val = root2.val)
                root3.left = dfs(None, root2.left)
                root3.right = dfs(None, root2.right)
            return root3
        
        return dfs(root1, root2)

# Time complexity: O(n)
# Space complexity: O(n)
# We can eliminate the elif statements by using the or operator.

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1, root2):
            if root1 and root2:
                root3 = TreeNode(val = root1.val + root2.val)
                root3.left = dfs(root1.left, root2.left)
                root3.right = dfs(root1.right, root2.right)
            elif not root1 and not root2:
                return None
            elif root1 or root2:
                root_valid = root1 if root1 else root2
                root3 = TreeNode(val = root_valid.val)
                root3.left = dfs(root_valid.left, None)
                root3.right = dfs(root_valid.right, None)
            return root3
        
        return dfs(root1, root2)

# Time complexity: O(n)
# Space complexity: O(n)
    
# Another way to solve this problem is to modify the original tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root1, root2):
            if root1 and root2:
                root1.val = root1.val + root2.val
                root1.left = dfs(root1.left, root2.left)
                root1.right = dfs(root1.right, root2.right)
                return root1
            elif root1 or root2:
                root_valid = root1 if root1 else root2
                root_valid.left = dfs(root_valid.left, None)
                root_valid.right = dfs(root_valid.right, None)
                return root_valid
            elif not root1 and not root2:
                return None
        
        return dfs(root1, root2)

# Time complexity: O(n)
