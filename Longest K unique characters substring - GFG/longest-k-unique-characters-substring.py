#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        i = j = 0
        maxLen = 0
        fMap = {}
        while j < len(s):
            fMap[s[j]] = fMap.get(s[j],0) + 1
            if len(fMap) > k:
                while len(fMap) > k:
                    fMap[s[i]] -= 1
                    if fMap[s[i]] == 0:
                        fMap.pop(s[i])
                    i += 1
    
            if len(fMap) == k:
                maxLen = max(maxLen,j-i+1)
                j += 1
            else:
                j += 1
        return maxLen if maxLen != 0 else -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends