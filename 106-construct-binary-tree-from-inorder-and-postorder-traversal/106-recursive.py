# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        for i in range(len(inorder)):
            if (inorder[i] == postorder[-1] and \
                    set(inorder[0:i]) == set(postorder[0:i]) and \
                    set(inorder[i+1:]) == set(postorder[i:-1])):
                
                left_inorder = inorder[0:i]
                left_postorder =  postorder[0:i]
                right_inorder = inorder[i+1:]
                right_postorder = postorder[i:-1]

                root = TreeNode(val = postorder[-1])
                root.left = self.buildTree(left_inorder,left_postorder)
                root.right = self.buildTree(right_inorder, right_postorder)

                return root

# Comment:
# The key point is to find the root node in the inorder list.
# Then we can divide the inorder list and postorder list into two parts.
# The left part is the left subtree and the right part is the right subtree.
# We can use recursive calls to build the tree.
# Time complexity: O(n^2) ? The set operation may take O(n) time.
# Space complexity: O(n)

# Check the problem again and the problem states that "inorder and postorder consist of unique values."
# So we can get rid of the set operation, and find the index of the root node directly.
# If we don't have the unique values condition, the set operation will not work properly
# for instance, construct the tree from [1,1,1,1,1] and [1,1,1,1,1] will not work
# With that being said, the set operation is not at all necessary in this problem.

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        idx_root = inorder.index(postorder[-1])
                
        left_inorder = inorder[0:idx_root]
        left_postorder =  postorder[0:idx_root]
        right_inorder = inorder[idx_root+1:]
        right_postorder = postorder[idx_root:-1]

        root = TreeNode(val = postorder[-1])
        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
