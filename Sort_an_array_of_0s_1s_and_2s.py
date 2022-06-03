class SortZeroOnesTwos:
    def __init__(self, items = []):
        self.nums = []
        for i in items:
            self.nums.append(i)

    def __swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        
    def sortarray(self):
        start = 0
        end = len(self.nums)-1
        i = 0
        while(i<=end):
            if self.nums[i] == 0:
                self.__swap(start, i)
                start += 1
                i += 1
            elif self.nums[i] == 2:
                self.__swap(end, i)
                end -= 1
            else:
                i += 1
    def display(self):
        return self.nums
