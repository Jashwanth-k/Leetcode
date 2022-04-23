class Solution:
    def splitCandies(self,candies,k,mid):
        for i in candies:
            k -= (i // mid)
            if k <= 0:
                return True
        return False
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        si,ei = 1,sum(candies)
        ans = 0
        while si <= ei:
            mid = si + (ei-si) // 2
            if self.splitCandies(candies,k,mid):
                ans = max(ans,mid)
                si = mid + 1
            else:
                ei = mid - 1
        return ans
            
            