class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        output = [0] * (n+1)
        output[1] = 1
        i, j = 2, 1
        
        if n == 1:
            return output
        
        while i <= n:
            output[i] = output[j]
            i+=1
            if i > n:
                break
            output[i] = output[j] + 1
            i += 1
            j += 1
        return output        