class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        stb = bin(start)[2:]
        mxlen = len(bin(2**n-1)[2:])
        st = "0"*(mxlen - len(stb)) + stb
        helper = [st]
        used = set()
        used.add(st)
        ct = 1
        while ct < 2**n:
            cur = helper[-1]
            for i in range(mxlen):
                change = cur[:i] + str(1 - int(cur[i])) + cur[i+1:]
                if change not in used:
                    helper.append(change)
                    used.add(change)
                    break
            ct += 1
        return [int(i,2) for i in helper]