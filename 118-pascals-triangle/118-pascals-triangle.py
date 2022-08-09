class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            singleRow = [1]*(i+1)
            for j in range(1, len(singleRow)-1):
                singleRow[j] = output[i-1][j-1] + output[i-1][j]
            output.append(singleRow)
            # print(singleRow)
        return output
            