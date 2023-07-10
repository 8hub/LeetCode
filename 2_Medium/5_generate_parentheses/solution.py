from typing import List

class Solution:
    def __init__(self) -> None:
        self.answer = ['(']

    def generateParenthesis(self, n: int) -> List[str]:
        while self.countClose(self.answer[0]) < n: #any to set to 0
            for index, each in enumerate(self.answer):
                open = self.countOpen(each)
                close = self.countClose(each)
                if close == n:
                    continue
                elif open == n:
                    self.answer[index] = "".join(each) +')'
                elif open > close:
                    self.answer.append("".join(each)+')')
                    self.answer[index] = "".join(each)+'('
                else:
                    self.answer[index] ="".join(each+'(')
                    
        return self.answer
    
    def countOpen(self, to_check: str) -> int:
        return to_check.count('(')
    
    def countClose(self, to_check: str) -> int:
        return to_check.count(')')

        

        
s1 = Solution()
s2= Solution()
s3 = Solution()
s4 = Solution()
s5 = Solution()
print(s1.generateParenthesis(1))
print(s2.generateParenthesis(2))
print(s3.generateParenthesis(3))
print(s4.generateParenthesis(4))

# ["(((())))","((()()))","((())())","(()(()))","(()()())",
# "((()))()","(()())()","(())()()",
# "()((()))","()(()())","()()(())",
# "(())(())","()(())()",
# "()()()()"]