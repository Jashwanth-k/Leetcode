class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 2:
            end = k+1 if k != 9 else 0
            start = 1 if end != 0 else k
            helper = [str(start) + str(end)]
            while True:
                start,end = int(helper[-1][0]),int(helper[-1][1])
                if start+1 == 10:
                    break
                if end+1 == 10:
                    helper.append(str(k) + "0")
                else:
                    helper.append(str(start+1) + str(end+1))
            return helper
                    
        smalloutput = self.numsSameConsecDiff(n-1,k)
        output = []
        for i in smalloutput:
            sub = int(i[-1]) - k
            add = int(i[-1]) + k
            if sub >= 0:
                output.append(i + str(sub))
            if add < 10:
                output.append(i + str(add))
        return set(output)