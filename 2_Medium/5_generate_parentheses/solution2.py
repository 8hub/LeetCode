from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(open, close) -> None:
            #base case
            if open == close == n:
                res.append("".join(stack))
                return
            if close < open:
                stack.append(')')
                backtrack(open, close+1)
                stack.pop()
            if open < n:
                stack.append('(')
                backtrack(open+1, close)
                stack.pop()
        backtrack(0,0)
        return res
    
s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))