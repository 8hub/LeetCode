class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        # root_val = root.val
        def dfs(node:TreeNode, previous:int):
            nonlocal counter
            if node == None:
                return
            if node.val >= previous:
                counter += 1
                previous = node.val
            dfs(node.left, previous)
            dfs(node.right, previous)
        dfs(root, root.val)
        return counter

sol = Solution()
tree1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4,TreeNode(1),TreeNode(5)))
tree2 = TreeNode(3, TreeNode(3,TreeNode(4), TreeNode(2)))
tree3 = TreeNode(1)
print(sol.goodNodes(tree1))
print(sol.goodNodes(tree2))
print(sol.goodNodes(tree3))
