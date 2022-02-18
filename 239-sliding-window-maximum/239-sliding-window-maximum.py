class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = j = 0
        output = []
        queue = collections.deque()
        while j < len(nums):
            while len(queue) != 0 and nums[j] > queue[-1]:
                queue.pop()
            queue.append(nums[j])
            if (j-i+1) == k:
                output.append(queue[0])
                if nums[i] == queue[0]:
                    queue.popleft()
                i += 1
                j += 1
            else:
                j += 1
        return output