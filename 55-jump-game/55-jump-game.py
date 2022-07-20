class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_reachable = len(nums)-1
        for j in range(len(nums)-2, -1, -1):
            if j+nums[j] >= last_reachable:
                last_reachable = j
        if last_reachable == 0:
            return True
        return False    