from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '-':
                stack[len(stack)-2] = stack[len(stack)-2] - stack[len(stack)-1]
                stack.pop()
            elif token == '+':
                stack[len(stack)-2] = stack[len(stack)-2] + stack[len(stack)-1]
                stack.pop()
            elif token == '*':
                stack[len(stack)-2] = stack[len(stack)-2] * stack[len(stack)-1]
                stack.pop()
            elif token == '/':
                stack[len(stack)-2] = int(stack[len(stack)-2] / stack[len(stack)-1])
                stack.pop()
            else:
                stack.append(int(token))
        return stack[0]

s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))