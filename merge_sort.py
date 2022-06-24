class MergeSort:
    def margesort(self, arr, n):
        temp_arr = [0]*n
        self._margesort(arr, temp_arr, 0, n-1)
        return arr
    
    def _margesort(self, arr, temp_arr, left, right):
        if left < right:
            mid = (left + right)//2
            self._margesort(arr, temp_arr, left, mid)
            self._margesort(arr, temp_arr, mid+1, right)
            self.marge(arr, temp_arr, left, mid, right)
    
    def marge(self, arr, temp_arr, left, mid, right):
        for i in range (left, right+1):
            temp_arr[i] = arr[i]
            
        left_idx = left
        right_idx = mid + 1
        currt = left
        
        while left_idx <= mid and right_idx <= right:
            if temp_arr[left_idx] <= temp_arr[right_idx]:
                arr[currt] = temp_arr[left_idx]
                left_idx += 1
            else:
                arr[currt] = temp_arr[right_idx]
                right_idx += 1
            currt += 1
        
        remining = mid - left_idx
        
        for j in range(remining+1):
            arr[currt+j] = temp_arr[left_idx + j]
            
ms = MergeSort()
print(ms.margesort([7,5,8,3,6,8,1,2],8))
