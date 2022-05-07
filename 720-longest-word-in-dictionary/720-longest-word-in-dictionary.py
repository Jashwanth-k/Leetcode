class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        wordDict = set(words)
        for word in words:
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                if all(word[:k] in wordDict for k in range(1,len(word))):
                    ans = word
        return ans