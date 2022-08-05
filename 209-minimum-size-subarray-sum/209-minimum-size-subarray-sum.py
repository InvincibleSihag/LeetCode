import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        res = math.inf
        curr_sum = 0
        prev_index = 0
        for i in range(0, length):
            curr_sum += nums[i]
            # print(prev_index, i, curr_sum)
            
            while curr_sum >= target and prev_index <= i:
                print(prev_index, i, curr_sum)
                if curr_sum >= target:
                    res = min(res, i-prev_index)
                curr_sum-=nums[prev_index]
                prev_index += 1
        return 0 if res==math.inf else res+1
    