class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted([0] + horizontalCuts + [h])
        verticalCuts = sorted([0] + verticalCuts + [w])
        maxH = maxV = 0
        for i in range(1,len(horizontalCuts)):
            maxH = max(maxH,horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            maxV = max(maxV,verticalCuts[i] - verticalCuts[i-1])
        return (maxH * maxV) % (10**9 + 7)