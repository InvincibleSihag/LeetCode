from collections import Counter
import copy
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = len(nums) - (len(nums) - len(set(nums)))
        for i, val in enumerate(Counter(nums).keys()):
            nums[i] = val
        return a