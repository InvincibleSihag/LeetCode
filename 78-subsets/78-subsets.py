class Solution:
    def helper(self, arr, subset, i):
        if len(arr) == i:
            self.subsetsList.append(list(subset))
            return
        else:
            subset.add(arr[i])
            self.helper(arr, subset, i+1)
            subset.remove(arr[i])
            self.helper(arr, subset, i+1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, set(), 0)
        return self.subsetsList
    
    def __init__(self):
        self.subsetsList = []
        