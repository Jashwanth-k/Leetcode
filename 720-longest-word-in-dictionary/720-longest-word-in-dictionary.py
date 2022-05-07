class Solution:    
    def longestWord(self, words: List[str]) -> str:
        n = len(words)
        ans = ""
        maxLen = 0
        for i in range(n):
            word1 = words[i]            
            x = len(word1)
            if x < maxLen:
                continue
            
            helper = words[i]
            while len(helper) != 0:
                helper = helper[:-1]
                if helper not in words:
                    break
                    
            if len(helper) == 0:
                if x > maxLen:
                    maxLen = x
                    ans = word1
                elif x == maxLen:
                    ans = min(ans,word1)
        return ans
                