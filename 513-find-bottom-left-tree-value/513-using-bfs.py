# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = [root,]
        while(queue):
            node = queue.pop(0)
            ans = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return ans

# Comment:
# This solution uses a level order traversal to find the leftmost element in the last level of the tree.
# At each level, we pop the first element from the queue and add its "right" and "left" children to the queue.
# The last element in the queue will be the leftmost element in the last level of the tree.