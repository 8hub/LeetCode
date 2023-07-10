from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #slow recursive
        max_depth = 0
        def countDepth(node, curr_layer):
            nonlocal max_depth
            if not node:
                return
            max_depth = max(max_depth,curr_layer)
            if node.left:
                countDepth(node.left, curr_layer+1)
            if node.right:
                countDepth(node.right, curr_layer+1)
        countDepth(root,1)
        return max_depth

        #fast recursive
        if not root:
            return 0
        return 1+max(maxDepth(root.left, root.right))

        #iterative using stack
        stack = [[root, 1]]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return max_depth