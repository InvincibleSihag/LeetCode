class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*n for i in range(m)]
        # print(arr)
        for i in range(n):
            arr[0][i] = 1
        for j in range(m):
            arr[j][0] = 1
        for q in range(1, m):
            for l in range(1, n):
                arr[q][l] = arr[q-1][l] + arr[q][l-1]
        return arr[-1][-1]
    