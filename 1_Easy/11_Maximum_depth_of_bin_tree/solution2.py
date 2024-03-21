from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr_depth = 0
        max_depth = 0
        def dfs(node:Optional[TreeNode], current_depth:int) -> TreeNode:
            nonlocal max_depth
            if node == None:
                current_depth -= 1
                return
            current_depth += 1
            max_depth = max(max_depth, current_depth)
            dfs(node.left, current_depth)
            dfs(node.right, current_depth)
        dfs(root, curr_depth)
        return max_depth

sol = Solution()
print(sol.maxDepth(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
print(sol.maxDepth(None))
print(sol.maxDepth(TreeNode(1)))
print(sol.maxDepth(TreeNode(0, None, TreeNode(1))))
print(sol.maxDepth(TreeNode(0, TreeNode(1), None)))
print(sol.maxDepth(TreeNode(0, TreeNode(1), TreeNode(2))))
print(sol.maxDepth(TreeNode(0,TreeNode(2,TreeNode(1,TreeNode(5),TreeNode(1)),None), TreeNode(4,TreeNode(3,None,TreeNode(6)),TreeNode(-1,None,TreeNode(8))))))