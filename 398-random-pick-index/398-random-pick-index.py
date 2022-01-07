class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.d = {}
        for i in range(len(nums)):
            self.d[nums[i]] = self.d.get(nums[i],[]) + [i]

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)