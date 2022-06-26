#  calculate maxReach 
#  if i reach to end return jump
#  if i > maxReach then its not possbile
#  
#
#

class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = nums[0]
        step = nums[0]
        jump = 1
        n = len(nums)
        
        if n <= 1:
            return 0
        
        if nums[0] == 0:
            return 0
            
        for i in range(1,n):
            if i == n-1:
                return jump
            
            if maxReach < i+nums[i]:
                maxReach = i+nums[i]
            
            step -= 1
            if step == 0:
                jump += 1
                
                if i>=maxReach:
                    return -1
                
                step = maxReach - i
