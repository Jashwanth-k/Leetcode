class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        dp = [[float('-inf')]*(m+1) for j in range(n+1)]
        output = float('-inf')
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                prod = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(prod + dp[i-1][j-1],dp[i][j-1],dp[i-1][j],prod)
                output = max(output,dp[i][j])
        return output