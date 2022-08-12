class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        output = []
        def helper(index, string):
            if len(string) == len(digits):
                output.append(string)
                return
            for ch in keys[digits[index]]:
                helper(index+1, string+ch)
            
                
        keys = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        helper(0, "")
        return output
        