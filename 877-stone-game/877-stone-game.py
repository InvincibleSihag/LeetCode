class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles.sort()
        alice_sum = 0
        bob_sum = 0
        for i, val in enumerate(piles):
            if i&1 == 0:
                alice_sum += val
            else:
                bob_sum += val
        return True if alice_sum > bob_sum else bob_sum
        