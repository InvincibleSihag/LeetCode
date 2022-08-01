class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Simple Methode
#         nums.sort()
#         return nums[int(len(nums)/2)]
    
        #Voting Method
        maj_count = 1
        maj_index = 0
        for i, val in enumerate(nums):
            if i == 0:
                continue
            if nums[i] == nums[maj_index]:
                maj_count += 1
            else:
                maj_count -= 1
            if maj_count < 1:
                maj_index = i
                maj_count = 1
        count = 0
        length = len(nums)
        for ele in nums:
            if ele == nums[maj_index]:
                count += 1
            if count > int(length/2):
                return nums[maj_index]
        return -1