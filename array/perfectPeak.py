# calculate max from left side and store in one array and then calcuate min from right side and store in array 
# and check if A[i] > left_side[i-1] and A[i]< right_side[i+1] return 1 or return 0
class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        found=False
        mxx = A[0]
        mnn = A[len(A)-1]
        left_gre=[A[0]]*(len(A))
        right_less=[A[-1]]*(len(A))
        for i in range(1,len(A)):
            mxx = max(A[i],mxx)
            left_gre[i] = mxx
        for i in range(len(A)-2,-1,-1):
            mnn = min(A[i],mnn)
            right_less[i] = mnn
        for i in range(1,len(A)-1):
            if A[i]>left_gre[i-1] and A[i]<right_less[i+1]:
                return 1
        return 0
