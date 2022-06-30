#User function Template for python3

class Solution:
    def arrangeTiles(self, N):
        M = N+5
        arr = [0]*M
        arr[0] = 1
        arr[1] = 1
        arr[2] = 1
        arr[3] = 1
        for i in range(4,N+1):
            arr[i] = arr[i-4] + arr[i-1]
        return arr[N]
