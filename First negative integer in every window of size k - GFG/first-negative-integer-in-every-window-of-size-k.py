#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    i = j = 0
    currList = []
    finalList = []
    while j < N:
        if A[j] < 0:
            currList.append(A[j])
        if (j-i+1) == K:
            if len(currList) == 0:
                finalList.append(0)
            else:
                finalList.append(currList[0])
                if currList[0] == A[i]:
                    currList.pop(0)
            i += 1
            j += 1
        else:
            j += 1
    return finalList
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends