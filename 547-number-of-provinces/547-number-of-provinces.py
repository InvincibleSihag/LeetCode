class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, j):
            isConnected[i][j] = -1
            isConnected[j][i] = -1
            for k in range(len(isConnected[0])):
                if isConnected[j][k] != -1 and isConnected[j][k] == 1:
                    if j == k:
                        isConnected[j][k] = -1
                    else:
                        dfs(j, k)
        count = 0
        for i in range(len(isConnected)):
            flag = False
            for j in range(len(isConnected[0])):        
                if isConnected[i][j] != -1 and isConnected[i][j] == 1:
                    if i == j:
                        isConnected[i][j] = -1
                    else:
                        dfs(i, j)
                    flag = True
            if flag:
                count += 1
        return count
                