class UnionIntersectionClass:
    def __init__(self, arr1 = [], arr2 = []):
        self.arr1 = []
        self.arr2 = []
        for i in arr1:
            self.arr1.append(i)
        
        for i in arr2:
            self.arr2.append(i)

    def find_instersecton(self):
        return list(set(self.arr1).intersection(set(self.arr2)))
    
    def find_union(self):
        arr1_set = set(self.arr1)
        arr1_set.update(set(self.arr2))
        return arr1_set
