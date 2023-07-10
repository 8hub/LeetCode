# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good_nodes_nr = 0
        def count_good_nodes(node, max_val):
            if node:
                if node.val >= max_val:
                    return 1+count_good_nodes(node.left, node.val) + count_good_nodes(node.right, node.val)
                return count_good_nodes(node.left, max_val) + count_good_nodes(node.right, max_val)
            return 0
        return count_good_nodes(root, root.val)

tree1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4,TreeNode(1),TreeNode(5)))
tree2 = TreeNode(3, TreeNode(3,TreeNode(4), TreeNode(2)))
s = Solution()
print(s.goodNodes(tree1))
print(s.goodNodes(tree2))