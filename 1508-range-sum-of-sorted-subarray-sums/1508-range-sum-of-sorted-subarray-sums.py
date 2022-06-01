class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        helper = []
        for size in range(1,n+1):
            i = 0
            currSum = 0
            for j in range(n):
                currSum += nums[j]
                if (j-i+1) == size:
                    helper.append(currSum)
                    currSum -= nums[i]
                    i += 1
        
        helper.sort()
        ans = 0
        for i in range(left-1,right):
            ans = (ans + helper[i]) % (10**9 + 7)
        return ans