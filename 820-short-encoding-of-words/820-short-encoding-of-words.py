class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        used = set()
        ans = 0
        words.sort(key=lambda x:-len(x))
        for w in words:
            if w not in used:
                n = len(w)
                for i in range(n):
                    used.add(w[i:])
                ans += n + 1
        return ans