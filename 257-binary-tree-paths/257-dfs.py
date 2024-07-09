# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct_path(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path) 
                else:
                    path += '->'
                    construct_path(root.left, path)
                    construct_path(root.right, path)
        paths = []
        construct_path(root, '')
        return paths

# Using DFS
# Time complexity: O(N), because we visit each node exactly once.
# Space complexity: O(N), where N is the number of nodes. The maximum depth of the recursion tree can be N, when the tree is skewed. 
# In average case, the depth will be log(N) for balanced tree.