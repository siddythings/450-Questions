class Solution:
    def subArraySum(self,arr, n, s): 
        sum = 0
        start = 0
        for i in range(n):
            sum += arr[i]
            
            while(sum>s):
                sum -= arr[start]
                start += 1
            
            if sum == s:
                return [start+1, i+1]
        
        return [-1]
