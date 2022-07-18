class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curz = i = ans = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                curz += 1
            while curz > k and i <= j:
                if nums[i] == 0:
                    curz -= 1
                i += 1
            ans = max(ans,j-i+1)
        return ans