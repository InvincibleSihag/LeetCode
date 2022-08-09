class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        pre_max = [0] * (length)
        pos_max = [0] * (length)
        pre_max[0] = height[0]
        pos_max[length-1] = height[length-1]
        
        for i, j in zip(range(1, length), range(length-2, -1, -1)):
            pre_max[i] = max(height[i], pre_max[i-1])
            pos_max[j] = max(height[j], pos_max[j+1])
        # print(pre_max)
        # print(pos_max)
        output = 0
        for i in range(length):
            output += min(pre_max[i], pos_max[i]) - height[i]
        return output
        