class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        totalFreq = [0]*7
        topFreq = [0]*7
        bottomFreq = [0]*7
        n = len(tops)
        for i in range(n):
            topVal,bottomVal = tops[i],bottoms[i]
            if topVal != bottomVal:
                totalFreq[bottomVal] += 1
            totalFreq[topVal] += 1
            topFreq[topVal] += 1
            bottomFreq[bottomVal] += 1

        ans = float("inf")
        for i in range(7):
            if totalFreq[i] == n:
                ans = min(totalFreq[i] - topFreq[i],totalFreq[i] - bottomFreq[i],ans)
        return ans if ans != float("inf") else -1