class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def DFS(i):
            if i < 0:
                if all(s == subsets[0] for s in subsets):
                    return True
                return False
            
            seen = set()
            for j in range(k):
                if subsets[j] in seen: continue
                if subsets[j] + nums[i] > self.target: continue
                seen.add(subsets[j])
                subsets[j] += nums[i]
                if DFS(i-1):
                    return True
                subsets[j] -= nums[i]
                
        self.tsum = sum(nums)
        if self.tsum % k != 0: return False
        self.target = self.tsum // k
        subsets = [0] * k
        return DFS(len(nums)-1)