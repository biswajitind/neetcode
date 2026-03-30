class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        newMin = val
        if len(self.minStack):
            newMin = self.minStack[-1]
        if val < newMin:
            newMin = val
        
        self.stack.append(val)
        self.minStack.append(newMin)        

    def pop(self) -> None:
        self.minStack.pop()
        return(self.stack.pop())
        
    def top(self) -> int:
        return(self.stack[-1])
        
    def getMin(self) -> int:
        return(self.minStack[-1])
        
