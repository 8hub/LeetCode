from typing import Optional
# from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        count = 0
        while stack and count != k:
            while stack[-1].left:
                stack.append(stack[-1].left)
            while count != k:
                count += 1
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                    break
        return node.val


s = Solution()
tree1 = TreeNode(7, TreeNode(3, TreeNode(2, TreeNode(1)),TreeNode(4,None,TreeNode(5))),TreeNode(9))
tree2 = TreeNode(7)
print(s.kthSmallest(tree1,7))
print(s.kthSmallest(tree2,1))