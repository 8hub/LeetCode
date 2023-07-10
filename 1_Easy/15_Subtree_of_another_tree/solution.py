from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root_node, subRoot_node):
            if not root_node and not subRoot_node:
                return True
            # OR work as XOR after AND above
            if not root_node or not subRoot_node:
                return False
            if root_node.val == subRoot_node.val:
                return check(root_node.left,subRoot_node.left) and check(root_node.right, subRoot_node.right)
            return False
        stack = [root]
        while stack:
            current_node = stack.pop()
            if check(current_node, subRoot):
                return True
            if current_node:
                stack.append(current_node.left)
                stack.append(current_node.right)
        return False

s = Solution()
tree1 = TreeNode(3, TreeNode(4,TreeNode(1),TreeNode(2)), TreeNode(5))
tree2 = TreeNode(4, TreeNode(1), TreeNode(2))
s.isSubtree(tree1,tree2)