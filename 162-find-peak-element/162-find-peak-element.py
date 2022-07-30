class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return ln-1
        
        left, right = 0, ln
        while left < right:
            mid = left + int((right-left)/2)
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] > nums[mid]:
                right = mid
            elif nums[mid+1] > nums[mid]:
                left = mid + 1
                
                