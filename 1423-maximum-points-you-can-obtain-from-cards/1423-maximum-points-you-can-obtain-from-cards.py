class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        totalSum = sum(cardPoints)
        if n == k: return totalSum
        minSum = float('inf')
        currSum = 0
        i,j = 0,0
        while j < n:
            currSum += cardPoints[j]
            if (j-i+1) == n - k:
                minSum = min(minSum,currSum)
                currSum -= cardPoints[i]
                i += 1
            j += 1
        return totalSum - minSum