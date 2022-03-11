class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        last = last2 = 0

        for i in range(n - 1, -1, -1):
            curr = cost[i] + min(last2,last)
            last = last2
            last2 = curr
        return min(curr,last)