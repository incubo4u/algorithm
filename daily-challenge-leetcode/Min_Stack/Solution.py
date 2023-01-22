class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2147483649
        
    def push(self, val: int) -> None:
        self.min = min(val,self.min)
        self.stack.append((val,self.min))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = 2147483649

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        