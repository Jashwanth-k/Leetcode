class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = [0]*26
        for i in s:
            frequencies[ord(i)-97] += 1
            
        deleteCount = 0
        frequencies.sort(reverse=True)
        for j in range(1, 26):
            if frequencies[j] >= frequencies[j-1]:
                if frequencies[j-1] == 0:
                    deleteCount += frequencies[j]
                    frequencies[j] = 0
                else:
                    deleteCount += frequencies[j] - (frequencies[j-1] - 1)
                    frequencies[j] = frequencies[j-1] - 1
        return deleteCount