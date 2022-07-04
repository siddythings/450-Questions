
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start = 0
        max_arr = []
        sums = 0
        maxx = float('-inf')
        temp_arr = []
        for i in range(len(A)):
            if A[i] >= 0:
                sums += A[i]
                temp_arr.append(A[i])
                if sums >= maxx:
                    if sums == maxx and len(max_arr)>len(temp_arr):
                        continue
                    maxx = sums
                    max_arr = temp_arr
            else:
                sums = 0
                temp_arr = []
        
        return max_arr
