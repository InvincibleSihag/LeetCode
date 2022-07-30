class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        if len(nums) == 1:
            return nums[0]
        while left<right:
            mid = left + int((right-left)/2)
            if mid == 0 and nums[len(nums)-1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[right-1] < nums[mid]:
                left = mid+1
            else:
                right = mid
            