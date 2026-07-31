class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        self.min = self.getMin() if self.stack else self.min
        self.min = min(self.min, value) if self.stack else value

        self.stack.append((value, self.min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()