class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def checkUsed(nums):
            if len(set(nums)) == len(nums) and all(used[ord(j)-97] == False for j in nums):
                return True
            return False
        
        def DFS(i):
            if i < 0:
                return 0
            
            inclu = float("-inf")
            if checkUsed(arr[i]):
                for j in arr[i]:
                    used[ord(j)-97] = True
                inclu = len(arr[i]) + DFS(i-1)
                for j in arr[i]:
                    used[ord(j)-97] = False
            exclu = DFS(i-1)
            return max(inclu,exclu)
            
        used = [False] * 26
        return DFS(len(arr)-1)