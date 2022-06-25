class BinarySearch:
    def search(self, arr, left, right, value):
        if left <= right:
            mid = (left + right) //2
            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                return self.search(arr, left, mid - 1, value)
            else:
                return self.search(arr, mid + 1, right, value)
        else:
            return "-1"
            
bs = BinarySearch()
print(bs.search([1,2,3,4,5,6,7,8],0,7,7))
        
