from collections import defaultdict
class Solution:   
                
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        memo = defaultdict(lambda: None)
        def helper(index):
            if index >= length:
                return 0
            if memo[index] is not None:
                return memo[index]
            results = [helper(i) + nums[index] for i in range(index+2, length)]
            res = nums[index] if not results else max(results)
            memo[index] = res
            return res
        
        return max(helper(0), helper(1))
    