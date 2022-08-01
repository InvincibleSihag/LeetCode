from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Solution with extra Space
        # s1 = deque()
        # s2 = deque()
        # for ch in s:
        #     if ch == "#":
        #         if s1:
        #             s1.pop()
        #     else:
        #         s1.append(ch)
        # for ch in t:
        #     if ch == "#":
        #         if s2:
        #             s2.pop()
        #     else:
        #         s2.append(ch)
        # return s1==s2
        
        # Solution with O(1) auxilary Space
        first_ptr, sec_ptr = len(s)-1, len(t)-1
        count_first, count_sec = 0, 0
        while first_ptr >= 0 or sec_ptr >= 0:

            if s[first_ptr] == "#":
                count_first += 1
                first_ptr -= 1
                continue
            
            if first_ptr >=0 and count_first > 0:
                first_ptr -= 1
                count_first -= 1
                continue
            
            if t[sec_ptr] == "#":
                count_sec += 1
                sec_ptr -= 1
                continue
            
            if sec_ptr >= 0 and count_sec > 0:
                count_sec -= 1
                sec_ptr -= 1
                continue
            
            if (first_ptr < 0 and sec_ptr >= 0) or (sec_ptr < 0 and first_ptr >= 0) or s[first_ptr] != t[sec_ptr]:
                return False
            first_ptr -= 1
            sec_ptr -= 1    
        return True
    