class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = set()
        def helper(comb, target, curr_i):
            
            if target == 0:
                output.add(tuple(comb))
                return
            
            elif target < 0:
                return
            
            prev = -1
            for i in range(curr_i, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                comb.append(candidates[i])
                helper(comb, target-candidates[i], i+1)
                comb.pop()
                prev = candidates[i]
        candidates.sort()
        helper([], target, 0)  
        return [list(x) for x in output]     