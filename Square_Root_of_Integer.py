class Solution:
    def sqrt(self, A):
        if A == 0 or A== 1:
            return A
        
        l = 0
        r = A
        res = 1
        last = 1
        
        while l < r:
            
            mid = (l + r) // 2
            if mid * mid == A:
                return mid
            elif mid * mid < A:
                l = mid + 1
            else:
                r = mid
            if mid * mid < A:
                last = mid
        return last
                            
