class Solution:
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeftIndex():
            i = 0
            j = len(nums)
            while i<j:
                mid = i + int((j-i)/2)
                if mid > 0 and nums[mid] == target and nums[mid-1] < target:
                    self.leftIndex = mid
                    break
                elif mid == 0:
                    if nums[mid] == target:
                        self.leftIndex = mid
                        break
                if nums[mid] < target:
                    i = mid+1
                else:
                    j = mid
                    
        def findRightIndex():
            i = 0
            j = len(nums)
            while i<j:
                mid = i + int((j-i)/2)
                if mid < len(nums)-1 and nums[mid] == target and nums[mid+1] > target:
                    self.rightIndex = mid
                    break
                elif mid == len(nums)-1:
                    if nums[mid] == target:
                        self.rightIndex = mid
                        break
                if nums[mid] > target:
                    j = mid
                else:
                    i = mid+1
                
        findLeftIndex()
        findRightIndex()
        return [self.leftIndex, self.rightIndex]
    
    def __init__(self):
        self.nums = []
        self.target = None
        self.leftIndex = -1
        self.rightIndex = -1
        