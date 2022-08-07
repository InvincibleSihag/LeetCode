from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        subsetsList = set()
        def helper(arr, subset, i):
            if len(nums) == i:
                new_dict = defaultdict(lambda:0)
                for ele in subset:
                    new_dict[ele] += 1
                newHash = []
                for key in sorted(new_dict.keys()):
                    newHash.append(str(key) + "-" + str(new_dict[key])) 
                tup = tuple(newHash)
                if tup not in subsetsList:
                    subsetsList.add(tup)
                    output.append(list(subset))
                return
            else:
                subset.append(arr[i])
                helper(arr, subset, i+1)
                subset.pop()
                helper(arr, subset, i+1)
        helper(nums, [], 0)
        return output