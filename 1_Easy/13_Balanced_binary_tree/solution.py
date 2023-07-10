from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = True
        def dfs(node):
            nonlocal answer
            if not node or not answer:
                return -1
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height-right_height)>1:
                answer = False
            return 1 + max(left_height, right_height)
        dfs(root)
        return answer
    
s = Solution()
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n6 = TreeNode(10)
n1.left, n1.right = n2, n3
n3.left, n3.right = n4, n5
n5.right = n6

print(s.isBalanced(n1))