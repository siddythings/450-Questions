class RyclicallyRotate:
    def __init__(self, arr1 = []):
        self.arr1 = []
        for i in arr1:
            self.arr1.append(i)
    def rotate(self,k):
        i = 0
        arr_len = len(self.arr1) - 1
        self.__swap(i, arr_len)
        self.__swap(i, k-1)
        self.__swap(k, arr_len)
        retunr self.arr1
        
    def __swap(self, i, j):
        while i < j:
            self.arr1[i], self.arr1[j] = self.arr1[j], self.arr1[i]
            i += 1
            j -= 1
