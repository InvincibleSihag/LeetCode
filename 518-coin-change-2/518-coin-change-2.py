from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(lambda: -1)
        def helper(amountLeft, denoms):
            if amountLeft == 0:
                return 1
            if amountLeft < 0 or len(denoms) == 0:
                return 0
            
            if memo[(amountLeft, denoms[0])] >= 0:
                return memo[(amountLeft, denoms[0])]
            
            res = helper(amountLeft-denoms[0], denoms) + helper(amountLeft, denoms[1:])
            memo[(amountLeft, denoms[0])] = res
            return res
        
        return helper(amount, coins)
        