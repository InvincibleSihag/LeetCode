class Solution:
    def tribonacci(self, n: int) -> int:
        asset = [0, 1, 1]
        a, b, c = asset[0], asset[1], asset[2]
        if n <= 2:
            return asset[n]
        i = 3
        while i <= n:
            a, b, c = b, c, a+b+c
            i+=1
        return c
        
    