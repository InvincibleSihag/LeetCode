from collections import Counter
from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = sorted(candidates)
        already_visited = defaultdict(lambda: -1)
        output = []
        def helper(candidates, comb, target, curr_i, counter):
            
            if target == 0:
                output.append(list(comb))
                
            elif target < 0:
                return False
            
            for i in range(len(candidates)):
                comb.append(candidates[i])
                helper(candidates[i:], comb, target-candidates[i], i, counter)
                comb.pop()
                
        counter = defaultdict(lambda: 0)
        helper(candidates, [], target, 0, counter)  
        return output
    