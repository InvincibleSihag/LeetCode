class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        alreadyDone = set()
        for i in range(len(nums)):
            target = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                twoSum = nums[left] + nums[right]
                if twoSum > -target:
                    right -= 1
                elif twoSum < -target:
                    left += 1
                else:
                    if (target, nums[left], nums[right]) not in alreadyDone:
                        output.append([target, nums[left], nums[right]])
                        alreadyDone.add((target, nums[left], nums[right]))
                    left += 1
                    right -= 1
        return output
    