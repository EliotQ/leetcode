class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        min_diff = float('inf')
        last_val = float('inf')
        node = root
        stack = []

        while(node or stack):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                min_diff = min(min_diff, abs(node.val - last_val))
                last_val = node.val
                node = node.right
        return min_diff

# Comment:
# Time complexity: O(n), because we visit every node once.
# Space complexity: O(1), because we only store the last value and the minimum difference.
# This is the iterative inorder traversal of a binary tree.