class Solution:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
    
    def pop(self):
        if len(self.heap)>2:
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bottomDown(1)
    
    def peek(self):
        if len(self.heap)>1:
            return self.heap[1]
        return False
    
    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[parent] < self.heap[index]:
                self.__swap(parent,index)
                self.__floatUp(parent)
    
    def __bottomDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        if index != largest:
            self.__swap(largest,index)
            self.__bottomDown(largest)
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in nums:
            self.push(i)
        for i in range(k-1):
            self.pop()
            
        return self.peek()
