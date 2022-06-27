class MaximumSubarray:
    def maxSubArray(self,nums = []):
        max_val = nums[0]
        sums = 0
        for i in nums:
            sums += i
            if sums < 0:
                sums = 0
            elif sums > max_val:
                max_val = sums
        return max_val    
