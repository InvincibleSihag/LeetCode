class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        MOD = 10**9 + 7
        for n in arr:
            dp[n] = 1
            
        for i, n in enumerate(arr):
            # print(dp)
            for j in range(i):
                if not(n % arr[j]) and n // arr[j] in dp:
                    dp[n] += dp[arr[j]] * dp[n//arr[j]]
                    dp[n] %= MOD
        return sum(dp.values()) % MOD
                    
#         def isFactTree(start_ind, cur_num):
#             if len(arr)-1 == start_ind:
#                 return 1
#             i, j = start_ind+1, len(arr)-1
#             flag = False
#             while i <= j:
#                 product = arr[i]*arr[j]
#                 if product > cur_num:
#                     j -= 1
#                 elif product < cur_num:
#                     i += 1
#                 else:
#                     flag = True
#                     break
#             if flag:
#                 return isFactTree(i, arr[i]) + isFactTree(j, arr[j]) + 1
#             return 1
        
#         output = 0
#         for k in range(len(arr)):
#             output += isFactTree(k, arr[k])
        return output        