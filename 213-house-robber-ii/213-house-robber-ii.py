class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 1:
            return 0
        if length == 1:
            return nums[0]
        
        def helperRob1(nums):
            rob1, rob2 = 0, 0
            
            for num in nums:
                newRob = max(rob1+num, rob2)
                rob1, rob2 = rob2, newRob
            return rob2
            
        return max(helperRob1(nums[1:]), helperRob1(nums[:-1]))
        
        
    