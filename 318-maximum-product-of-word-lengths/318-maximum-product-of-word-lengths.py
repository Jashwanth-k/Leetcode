class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        helper = []
        for i in words:
            helper.append(set(i))
            
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                s1,s2 = helper[i],helper[j]
                if len(s1 & s2) == 0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans