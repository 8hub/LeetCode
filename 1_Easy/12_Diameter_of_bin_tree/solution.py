from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # O(N) solution -> from the bottom calculate diameter of each node
        # save diameter and height of each subtree
        # diameter = height_l + 1 + height_r + 1    , where height of None Node == -1
        max_diameter = 0
        #calculates max height of left and right and for each node update the max_diameter
        def max_height_and_update_max_diameter(node):
            if not node:
                return -1
            left_max_height = max_height_and_update_max_diameter(node.left)
            right_max_height = max_height_and_update_max_diameter(node.right)
            max_diameter = max(max_diameter, 2 + left_max_height + right_max_height)
            return 1 + max(left_max_height, right_max_height)
        max_height_and_update_max_diameter(root)
        return max_diameter
        '''
        # O(N^2) solution -> for each node calculate max height left + max height right
        max_diameter = 0
        def max_height(root):
            if not root:
                return 0
            return 1 + max(max_height(root.left), max_height(root.right))
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                max_diameter = max(max_diameter, max_height(node.left)+max_height(node.right))
                stack.append(node.left)
                stack.append(node.right)
        return max_diameter
        '''