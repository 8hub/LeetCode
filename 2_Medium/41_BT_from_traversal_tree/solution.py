from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#preorder tree go through nodes: root -> left -> right
# inorder tree go through nodes: left -> root -> right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        #number of nodes in left subtree
        left_nodes_number = inorder.index(preorder[0])
        if (left_nodes_number > 0):
            root.left = self.buildTree(preorder[1:left_nodes_number+1],inorder[:left_nodes_number])
        else:
            root.left = None
        right_nodes_number = len(inorder)-(left_nodes_number+1)
        if (right_nodes_number > 0):
            root.right = self.buildTree(preorder[-right_nodes_number:], inorder[-right_nodes_number:])
        else:
            root.right = None
        return root