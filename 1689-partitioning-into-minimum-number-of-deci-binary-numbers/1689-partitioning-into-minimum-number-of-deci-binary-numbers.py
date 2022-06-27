class Solution:
    def minPartitions(self, n: str) -> int:
        maxim = 0
        for i in n:
            maxim = max(maxim,ord(i) - 48)
        return maxim