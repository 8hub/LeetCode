from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        #recursive solution
        root.left , root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        #iterative solution
        stack = [root]
        while stack:
            curr_layer = stack.pop()
            curr_layer.left, curr_layer.right = curr_layer.left, curr_layer.right 
            if curr_layer.left:
                stack.append(curr_layer.left)
            if curr_layer.right:
                stack.append(curr_layer.right)
        return root