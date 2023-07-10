from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque = []
        if root:
            deque.append(root)
        order_list = []
        while deque:
            curr_level_len = len(deque)
            curr_level_nodes = []
            for elem_nr in range(curr_level_len):
                if deque[elem_nr]:
                    curr_level_nodes.append(deque[elem_nr].val)
                    deque.append(deque[elem_nr].left)
                    deque.append(deque[elem_nr].right)
            # drop checked level elements
            deque = deque[curr_level_len:]
            order_list.append(curr_level_nodes)
        if len(order_list) > 1:
            order_list.pop()
        return order_list

s = Solution()
tree = TreeNode(3,TreeNode(9), TreeNode(20,TreeNode(15), TreeNode(7)))
print(s.levelOrder(tree))