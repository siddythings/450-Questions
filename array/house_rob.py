# NEETCODE

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for obj in nums:
            temp = max(rob1+obj,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
