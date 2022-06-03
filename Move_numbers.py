class MoveNumbers:
    def __init__(self, items = []):
        self.nums = []
        for i in items:
            self.nums.append(i)

    def __swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        
    def move(self):
        start = 0
        for i in range(len(self.nums)):
            if self.nums[i] < 0:
                self.__swap(i,start)
                start += 1
                
    def display(self):
        return self.nums
