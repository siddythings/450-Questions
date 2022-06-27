class MinHeap:
    def __init__(self, arr=[]):
        self.heap = [0]
    
    def __swap(self, a,b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
    
    def __floatUp(self, index):
        prt = index//2
        
        if index<=1:
            return 
        elif self.heap[index]<self.heap[prt]:
            self.__swap(index,prt)
            self.__floatUp(prt)
    
    def __floatDown(self, index):
        left_c = index * 2
        right_c = index * 2 + 1
        smallest = index
        
        if len(self.heap) > left_c and self.heap[left_c] < self.heap[smallest]:
            smallest = left_c
        
        if len(self.heap) > right_c and self.heap[right_c] < self.heap[smallest]:
            smallest = right_c
        
        if smallest != index:
            self.__swap(index,smallest)
            self.__floatDown(smallest)
        
    def pop(self):
        self.__swap(1,len(self.heap)-1)
        min = self.heap.pop()
        self.__floatDown(1)
        return min
