import math
class Solution:
    def findChange(self, current, coins):
        if current == 0:
            return 0
        if current < 0:
            return math.inf
        if self.memo.get(current) is not None:
            return self.memo[current]
        # result = min([self.findChange(current-x, coins) for x in coins])
        mini = math.inf
        for x in coins:
            res = self.findChange(current-x, coins)
            # self.memo[current-x] = res
            if res < mini:
                mini = res
        self.memo[current] = mini + 1
        return self.memo[current]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Dynamic Tabulation Solution
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
        # Simple Dynamic Solution
        output = self.findChange(amount, coins)
        if output == math.inf:
            return -1
        return output
    
    def __init__(self):
        self.memo = {}
        