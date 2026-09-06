class MinStack:

    def __init__(self):
        self.stack = []
        self.head = -1

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
            
        else:
            currmin = self.getMin()
            if val < currmin:
                self.stack.append([val, val])
            else:
                self.stack.append([val, currmin])
        
        self.head+=1

    def pop(self) -> None:
        self.stack.pop()
        self.head-=1

    def top(self) -> int:
        
        return self.stack[self.head][0]

    def getMin(self) -> int:
        return self.stack[self.head][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()