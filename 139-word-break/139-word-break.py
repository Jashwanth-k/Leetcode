class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def word(s, wordDict, start, n):
            if n == 0:
                return True
            if (start,n) in dp:
                return dp[start,n]

            for i in range(len(wordDict)):
                end = len(wordDict[i])
                if s[start:start + end] == wordDict[i]:
                    pick = word(s, wordDict,start+end, n - end)
                    if pick:
                        dp[start,n] = pick
                        return pick
            dp[start,n] = False
            return False

        n = len(s)
        dp = {}
        return word(s, wordDict, 0, n)