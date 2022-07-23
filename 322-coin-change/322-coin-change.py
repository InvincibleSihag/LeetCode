import math
class Solution:
    def findChange(self, current, coins):
        if current == 0:
            return 0
        if current < 0:
            return math.inf
        if self.memo.get(current) is not None:
            return self.memo[current]
        result = min([self.findChange(current-x, coins) for x in coins])
        self.memo[current] = result + 1
        return self.memo[current]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        output = self.findChange(amount, coins)
        if output == math.inf:
            return -1
        return output
    
    def __init__(self):
        self.memo = {}
        