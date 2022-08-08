from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        start = end = 0
        n = len(nums)
        # prefix_sum = [0]*n+1
        # prefix_sum[0] = 0
        # for i in range(n):
        #     prefix_sum[i+1] = prefix_sum[i-1] + nums[i]
        pre_sum_dict = defaultdict(lambda: [])
        pre_sum_dict[0] = [-1]
        prefix_sum = 0
        count = 0
        for i in range(n):
            prefix_sum += nums[i]
            key = prefix_sum - k
            if pre_sum_dict[key] != []:
                count += len(pre_sum_dict[key])
            pre_sum_dict[prefix_sum].append(i)
        return count
                
        