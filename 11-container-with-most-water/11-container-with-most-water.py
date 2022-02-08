class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxwater = float('-inf')
        while i < j:
            ans = min(height[i],height[j])
            maxwater = max(maxwater,ans*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxwater