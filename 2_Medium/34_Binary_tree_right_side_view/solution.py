from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #have to append ans array with last element of each level...
        deque = [root]
        ans = []
        while deque:
            curr_rightmost = int
            length = len(deque)
            for elem in range(length):
                curr_node = deque.pop(0)
                if curr_node:
                    deque.append(curr_node.left)
                    deque.append(curr_node.right)
                    curr_rightmost = curr_node.val
                if elem == length - 1 and curr_rightmost is not int:
                    ans.append(curr_rightmost)
        return ans
    
s = Solution()
tree = TreeNode(3,TreeNode(9), TreeNode(20,TreeNode(15), TreeNode(7)))
print(s.rightSideView(tree))
print(s.rightSideView(TreeNode(None)))