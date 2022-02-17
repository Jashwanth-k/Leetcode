#User function Template for python3
class Solution:
	def search(self,pat, txt):
	    i = j = 0
        count = 0
        k = len(pat)
        dwindow = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        danag = {}
        for s in pat:
            danag[s] = danag.get(s,0) + 1

        while j < len(txt):
            dwindow[txt[j]] += 1
            if (j - i + 1) == k:
                for s in danag:
                    if danag[s] != dwindow[s]:
                        break
                else:
                    count += 1
                dwindow[txt[i]] -= 1
                i += 1
                j += 1
            else:
                j += 1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends