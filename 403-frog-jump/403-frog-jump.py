class Solution:
    def binarySearch(self,nums,si,ei,tar):
        while si <= ei:
            mid = si + (ei-si) // 2
            if nums[mid] == tar:
                return mid
            elif tar > nums[mid]:
                si = mid + 1
            else:
                ei = mid - 1
        return False
    
    def canCross(self, stones: List[int]) -> bool:
        def crossHelper(stones,i,n,k,dp):
            if i == n-1:
                return True
            if (i,k) in dp:
                return dp[i,k]
            
            ans1 = ans2 = ans3 = False
            zero = stones[i] + k
            idx = self.binarySearch(stones,i+1,n-1,zero)
            if idx:
                ans1 = crossHelper(stones,idx,n,k,dp)
            
            one = stones[i] + k+1
            idx = self.binarySearch(stones,i+1,n-1,one)
            if idx:
                ans2 = crossHelper(stones,idx,n,k+1,dp)
            
            mone = stones[i] + k-1
            idx = self.binarySearch(stones,i+1,n-1,mone)
            if idx:
                ans3 = crossHelper(stones,idx,n,k-1,dp)
            dp[i,k] = ans1 or ans2 or ans3
            return dp[i,k]
            
        n = len(stones)
        dp = {}
        return crossHelper(stones,0,n,0,dp)