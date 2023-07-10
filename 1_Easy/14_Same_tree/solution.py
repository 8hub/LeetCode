from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Using recursion
        if (not p and not q):
            return True
        #before is AND so this works as a XOR
        if (not p or not q):
            return False
        if (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
            
        
        # # Using iteration and stack
        # stack_p = [p]
        # stack_q = [q]
        # while (stack_p):
        #     p_node = stack_p.pop()
        #     q_node = stack_q.pop()
        #     # p_node XOR q_node
        #     if (p_node and not q_node) or (q_node and not p_node):
        #         return False
        #     if not p_node:
        #         continue
        #     if p_node and (p_node.val != q_node.val):
        #         return False
        #     stack_p.append(p_node.left)
        #     stack_p.append(p_node.right)
        #     stack_q.append(q_node.left)
        #     stack_q.append(q_node.right)
        # return True
            