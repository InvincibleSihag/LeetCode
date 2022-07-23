
class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = []
        last_index = len(nums)-1
        if last_index == 0 and nums[0] <= 1:
            return 0
        queue.append(0)
        steps = 0
        while queue:
            flag = False
            size = len(queue)
            for element in list(queue):
                if queue[-1] < element + nums[element]:
                    for i in range(queue[-1]+1, element + nums[element]+1):
                        if i >= last_index:
                            steps += 1
                            flag = True
                            break
                        queue.append(i)
                if flag:
                    break
            if flag:
                break
            queue = queue[size:]
            steps += 1
        return steps 
            