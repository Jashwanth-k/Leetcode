#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if m < n:
            return self.kthElement(arr2, arr1, m ,n, k)
        si, ei = 0, n - 1
        while si <= ei:
            mid = si + (ei - si) // 2
            cut = k - (mid + 1)
            l1 = arr1[mid]
            if cut > m:
                si = mid + 1
                continue
            if cut < 0:
                ei = mid - 1
                continue
            l2 = arr2[cut - 1] if cut - 1 >= 0 else float("-inf")
            r1 = arr1[mid + 1] if mid + 1 < n else float("inf")
            r2 = arr2[cut] if cut < m else float("inf")
            if l1 > r2:
                ei = mid - 1
            elif l2 > r1:
                si = mid + 1
            else:
                return max(l1, l2)
        return arr2[k - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends