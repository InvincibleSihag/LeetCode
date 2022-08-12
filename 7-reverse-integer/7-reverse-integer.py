class Solution:
    def reverse(self, x: int) -> int:
        reverse = str(x)[::-1]
        if reverse[-1] == "-":
            reverse = -int(reverse[:-1])
        else:
            reverse = int(reverse)
        return reverse if reverse in range(-2147483648, 2147483647) else 0