
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        arr = []
        prev = 1
        arr.append(prev)
        
        for i in range(1,A+1):
            x = (prev*(A-i+1))//i
            arr.append(x)
            prev = x
        return arr
        
