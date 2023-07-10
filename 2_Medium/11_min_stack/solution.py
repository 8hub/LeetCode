class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        try:
            self.stack.append(val)
        except:
            return None

    def pop(self) -> None:
        try:
            self.stack.pop()
        except:
            return None

    def top(self) -> int:
        try:
            return self.stack[len(self.stack)-1]
        except:
            return None
        
    def getMin(self) -> int:
        try:
            return min(self.stack)
        except:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(5)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

