from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = set()
        vector = [(1, 1), (1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        def bfs(index_r, index_c):
            queue = deque()
            queue.append((index_r, index_c))
            
            while queue:
                curr = queue.popleft()
                # print(curr)
                for vec in vector:
                    new_r, new_c = vec[0] + curr[0], vec[1] + curr[1]
                    if r > new_r > -1 and c > new_c > -1 and grid[new_r][new_c] < 1:
                        if (new_r, new_c) in visited:
                            continue
                        if grid[new_r][new_c] == 0:
                            grid[new_r][new_c] = grid[curr[0]][curr[1]]-1
                        elif grid[curr[0]][curr[1]] - 1 > grid[new_r][new_c]:
                            grid[new_r][new_c] -= grid[curr[0]][curr[1]]-1
                        # grid[new_r][new_c]-1
                        if new_r == r-1 and new_c == c-1:
                            print("returning")
                            return -1 if grid[new_r][new_c] == 0 else grid[new_r][new_c] - 1
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            return 1
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        if r==1 and c==1 and grid[0][0] == 0:
            return 1
        return -bfs(0, 0)
        