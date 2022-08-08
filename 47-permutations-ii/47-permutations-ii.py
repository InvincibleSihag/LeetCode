class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = set()
        visited = set()
        n = len(nums)
        def helper(arr, perm):
            if len(perm) == n:
                output.add(tuple(perm))
            for i in range(len(arr)):
                if i not in visited:
                    visited.add(i)
                    perm.append(arr[i])
                    helper(arr, perm)
                    perm.pop()
                    visited.remove(i)
        helper(sorted(nums), [])
        return [list(x) for x in output]