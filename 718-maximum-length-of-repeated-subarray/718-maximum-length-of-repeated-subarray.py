class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        dp = [[0]*(m+1) for j in range(n+1)]
        output = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1] == nums2[j-1]:
                    ans = 1 + dp[i-1][j-1]
                else:
                    ans = 0
                dp[i][j] = ans
                output = max(output,ans)
        return output