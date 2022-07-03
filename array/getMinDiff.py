# sort the array first store maxx, minn and there diff and then calculate diff of all the cobination of 
# max(arr[n-1]-k,arr[i]+k)
# min(arr[0]+k,arr[i]-k)
# diff = min(diff, maxx-minn)

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        maxx = arr[n-1]
        minn = arr[0]
        diff = maxx-minn
        for i in range(1,n):
            if arr[i]-k<0:
                continue
            maxx = max(arr[n-1]-k,arr[i-1]+k)
            minn = min(arr[0]+k,arr[i]-k)
            diff = min(diff, maxx-minn)
        return diff
