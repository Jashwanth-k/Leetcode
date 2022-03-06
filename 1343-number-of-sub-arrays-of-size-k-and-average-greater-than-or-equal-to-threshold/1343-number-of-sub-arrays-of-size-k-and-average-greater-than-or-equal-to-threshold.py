class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = j = 0
        currSum = 0
        output = 0
        while j < len(arr):
            currSum += arr[j]
            if (j-i+1) == k:
                if currSum // k >= threshold:
                    output += 1
                currSum -= arr[i]
                i += 1
            j += 1
        return output