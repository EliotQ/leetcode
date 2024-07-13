from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         queue = []
#         ans = []
#         queue.append([root,])

#         while(queue[0]):
#             node_this_level = queue.pop(0)
#             val_this_level = []
#             node_next_level = []
#             while(node_this_level):
#                 node = node_this_level.pop(0)
#                 val_this_level.append(node.val)
#                 if node.left:
#                     node_next_level.append(node.left)
#                 if node.right:
#                     node_next_level.append(node.right)
#             ans.append(val_this_level)
#             queue.append(node_next_level)
        
#         return ans

# Comment:
# Here the queue is a list of one element, which is a list of nodes of the current level.
# The while loop will end when the last level has no nodes.
# The time complexity is O(n), where n is the number of nodes in the tree.
# The space complexity is O(n) as well.

# Instead, we can replace the queue with a list of nodes of the next level (node_next_level)
# Fail to note the fact that the queue is a list of one element, even the element is empty, has led to the wrong condition of 
# while(queue) in the previous attempt.
# [[]] is regarded as True, 
# [] is regarded as False.
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        node_next_level = [root,]

        while(node_next_level):
            node_this_level = node_next_level
            val_this_level = []
            node_next_level = []
            while(node_this_level):
                node = node_this_level.pop(0)
                val_this_level.append(node.val)
                if node.left:
                    node_next_level.append(node.left)
                if node.right:
                    node_next_level.append(node.right)
            ans.append(val_this_level)
        
        return ans

# Test
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().levelOrder(root)
    print(result)