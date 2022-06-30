# First we loop from left side of the arr and try to find out the max element and there index and store the sum and copy the sum value
# to total value every time when we get any max 

# Second loop from right side from max value index to n to check weather if we have any small water block after max block
class Solution:
    def trappingWater(self, arr,n):
        total = 0
        temp = [0]*n
        max_val = arr[0]
        max_index = 0
        sums = 0
        for i in range(1,n):
            if max_val > arr[i]:
                sums += (max_val - arr[i])
                temp[i] = max_val - arr[i]
            else:
                max_val = arr[i]
                max_index = i
                total += sums
                sums = 0
        
        temp_max = arr[n-1]
        temp_sum = 0
        for i in reversed(range(max_index,n-1)):
            if temp_max > arr[i]:
                temp_sum += (temp_max - arr[i])
            else:
                temp_max = arr[i]
        return total+temp_sum
