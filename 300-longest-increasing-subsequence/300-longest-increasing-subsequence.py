from collections import defaultdict
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        # n = len(nums)
        # memo = defaultdict(lambda: -1)
        # def helper(cur_i):
        #     if memo[cur_i] != -1:
        #         return memo[cur_i]
        #     if cur_i == n-1:
        #         return 1
        #     res = 1
        #     flag = False
        #     for i in range(cur_i+1, n):
        #         if nums[i] > nums[cur_i]:
        #             flag = True
        #             res = max(res, helper(i)+1)
        #     memo[cur_i] = res
        #     return res
        # res = 0
        # for i in range(n):
        #     res = max(res, helper(i))
        #     memo[i] = res 
        # return res
    
        # Iterative Solution
        n = len(arr)
 
        # Declare the list (array) for LIS and
        # initialize LIS values for all indexes
        lis = [1]*n

        # Compute optimized LIS values in bottom up manner
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j]+1

        # Initialize maximum to 0 to get
        # the maximum of all LIS
        maximum = 0

        # Pick maximum of all LIS values
        for i in range(n):
            maximum = max(maximum, lis[i])

        return maximum
    