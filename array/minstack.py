class MinStack:

    def __init__(self):
        self.arr = []
        self.arr_max = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.arr_max:
            if self.arr_max[-1] < val:
                self.arr_max.append(self.arr_max[-1])
            else:
                self.arr_max.append(val)
        else:
            self.arr_max.append(val)
        return None
    
    def pop(self) -> None:
        self.arr.pop()
        self.arr_max.pop()
        return None
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.arr_max[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
