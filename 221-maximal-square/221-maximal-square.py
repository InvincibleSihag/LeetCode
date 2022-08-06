class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_sqr = -float("inf")
        vector = [(-1, 0), (-1, -1), (0, -1)]
        if "1" in matrix[0]:
            max_sqr = 1
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                max_sqr = 1
                break
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    flag = True
                    maximum = -float("inf")
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1]))+1
                    max_sqr = max(max_sqr, matrix[i][j])
        # print(matrix)
        return 0 if max_sqr == -float("inf") else max_sqr*max_sqr
                    