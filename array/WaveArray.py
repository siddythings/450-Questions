# sort the array and swap A[i] to A[i+1] element

class Solution:
    def convertToWave(self, n : int, A : List[int]) -> None:
        A.sort()
        n = len(A)-2
        i = 0
        while n >= 0:
            A[i], A[i+1] = A[i+1], A[i]
            n -= 2
            i += 2
        return A
        
