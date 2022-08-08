from collections import defaultdict
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = defaultdict(lambda: -1)
        def helper(cur_i):
            if memo[cur_i] != -1:
                return memo[cur_i]
            if cur_i == n-1:
                return 1
            res = 1
            flag = False
            for i in range(cur_i+1, n):
                if nums[i] > nums[cur_i]:
                    flag = True
                    res = max(res, helper(i)+1)
            memo[cur_i] = res
            return res
        res = 0
        for i in range(n):
            res = max(res, helper(i))
            memo[i] = res 
        return res
    