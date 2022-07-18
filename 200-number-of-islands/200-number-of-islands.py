from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        move_vec = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        count = 0
        m = len(grid)
        n = len(grid[0])
        def find_conn(grid, indexes, visited, move_vec, m, n):
            visited.add(indexes)
            for vec in move_vec:
                new_indexes = (indexes[0]+vec[0], indexes[1]+vec[1])
                if 0 <= new_indexes[0] < m and 0 <= new_indexes[1] < n and new_indexes not in visited and grid[new_indexes[0]][new_indexes[1]] == "1": 
                    find_conn(grid, new_indexes, visited, move_vec, m, n)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i, j) not in visited:
                    count += 1
                    find_conn(grid, (i, j), visited, move_vec, m, n)
        return count