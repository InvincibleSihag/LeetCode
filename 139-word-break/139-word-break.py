from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set()
        memo = defaultdict(lambda: None)
        for word in wordDict:
            word_dict.add(word)
        
        def break_(s1, s2):
            if len(s2) == 1 and s2 not in word_dict:
                return False
            elif len(s2) == 1 and s1 in word_dict:
                return True
            elif len(s2) == 1:
                return False
            if memo[s1+s2] is not None:
                return memo[s1+s2]
            if s1 in word_dict and s2 in word_dict:
                return True
            if s1 in word_dict:
                r1 = break_(s2[:1], s2[1:])
                memo[s2] = r1
                r2 = break_(s1+s2[:1], s2[1:])
                memo[s1+s2[:1] + s2[1:]] = r2
                return r1 or r2 
            r3 = break_(s1+s2[:1], s2[1:])
            memo[s1+s2[:1], s2[1:]] = r3
            return r3
        
        if s in word_dict:
            return True
        elif len(s) == 1:
            return False
        return break_(s[:1], s[1:])