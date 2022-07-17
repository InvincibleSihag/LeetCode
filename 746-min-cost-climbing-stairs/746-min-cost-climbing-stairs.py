class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[-1] = 0
        dp[-2] = cost[-1]
        for j in range(len(cost)-2, -1, -1):
            dp[j] = cost[j] + min(dp[j+1], dp[j+2])
        return min(dp[0], dp[1])