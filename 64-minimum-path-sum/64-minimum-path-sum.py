from collections import defaultdict
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        memo = defaultdict(lambda: -1)
        
        def is_valid(i, j):
            if -1 < i < r and -1 < j < c:
                return True
            return False
        
        def minSum(i, j):
            if memo[(i, j)] != -1:
                return memo[(i, j)]
            if not is_valid(i, j):
                return float("inf")
            if i == r-1 and j == c-1:
                return grid[i][j]
            res = min(minSum(i+1, j), minSum(i, j+1)) + grid[i][j] 
            memo[(i, j)] = res
            return res
        return minSum(0, 0)
    