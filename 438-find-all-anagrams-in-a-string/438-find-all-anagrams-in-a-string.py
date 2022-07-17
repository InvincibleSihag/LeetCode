from collections import defaultdict, deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = deque()
        smallHash = defaultdict(lambda: 0)
        for ch in p:
            smallHash[ch] += 1
        queueHash = defaultdict(lambda: 0)
        for ch in s[0: len(p)]:
            queueHash[ch] += 1
        if queueHash == smallHash:
            output.append(0)
        queueHash[s[0]] -= 1
        if queueHash[s[0]] == 0:
            del queueHash[s[0]]
        prev = 1
        for i in range(len(p), len(s)):
            queueHash[s[i]] += 1
            if queueHash == smallHash:
                output.append(prev)
            queueHash[s[prev]] -= 1
            if queueHash[s[prev]] == 0:
                del queueHash[s[prev]]
            prev += 1
            # print(queueHash)
        return output
            