from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        for i, num in enumerate(nums):
            if diction.get(num) is not None:
                return [diction.get(num), i]
            diction[target-num] = i
        
        
        