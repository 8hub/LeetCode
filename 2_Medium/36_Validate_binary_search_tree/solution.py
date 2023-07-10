from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #have to add evaluation if I go to left node and from it to next right,
        #so the bottom right value is less then first top element value
            #     10
            #    /  \
            #   5    12
            #    \
            #     7  <= this value has to be less than 10
        #and similar evaluation has to be done going to right and then to left
        #there has to be checked if bottom value is still greater than top value
            #     10
            #    /  \
            #   5    12
            #       /
            #      11   <= this value has to be greater than 10 
        #solution done by lowering the range of possible value in which it can be
        def checkBTS(node, min, max):
            if not node:
                return True
            left_subtree = True
            right_subtree = True
            if node.left:
                if node.left.val > min and node.left.val < node.val:
                    left_subtree = checkBTS(node.left, min, node.val)
                else:
                    return False
            if node.right:
                if node.right.val > node.val and node.right.val < max:
                    right_subtree = checkBTS(node.right, node.val, max)
                else:
                    return False
            return left_subtree and right_subtree
        return checkBTS(root, -math.inf, math.inf)

            

s = Solution()
tree1 = TreeNode(10,TreeNode(5),TreeNode(15,TreeNode(11)))
print(s.isValidBST(tree1))      #True
tree2 = TreeNode(10,TreeNode(5),TreeNode(15,TreeNode(9)))
print(s.isValidBST(tree2))      #False
tree3 = TreeNode(32,TreeNode(26, TreeNode(19,right=TreeNode(27))),TreeNode(47,right=TreeNode(56, TreeNode(48))))
print(s.isValidBST(tree3))      #False
tree4 = TreeNode(2,TreeNode(2),TreeNode(2))
print(s.isValidBST(tree4))      #False
tree5 = TreeNode(0,TreeNode(),TreeNode(-1))
print(s.isValidBST(tree5))      #False
tree6 = TreeNode(120,TreeNode(70, TreeNode(50, TreeNode(20), TreeNode(55)), TreeNode(100, TreeNode(75), TreeNode(110))),TreeNode(140, TreeNode(130, TreeNode(119), TreeNode(135)), TreeNode(160, TreeNode(150), TreeNode(200))))
print(s.isValidBST(tree6))      #False
