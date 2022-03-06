class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = j = 0
        prevSub = set()
        output = set()
        while j < len(s):
            if (j-i+1) == 10:
                currSub = s[i:j+1]
                if currSub in prevSub:
                    output.add(currSub)
                prevSub.add(currSub)
                i += 1
            j += 1
        return output