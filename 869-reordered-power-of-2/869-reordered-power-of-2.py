class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        freq = Counter(str(n))
        i = 1
        while i <= 10**9:
            if Counter(str(i)) == freq:
                return True
            i *= 2
        return False