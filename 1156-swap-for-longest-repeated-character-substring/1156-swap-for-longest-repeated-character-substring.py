class Solution:
    def maxRepOpt1(self, text: str) -> int:
        i,res = 0,1
        curd = defaultdict(int)
        totalfreq = Counter(text)

        for j in range(len(text)):
            curd[text[j]] += 1
            while len(curd) > 2:
                curd[text[i]] -= 1
                if curd[text[i]] == 0:
                    curd.pop(text[i])
                i += 1
            if len(curd) == 2:
                chr1,chr2 = list(curd.keys())
                while len(curd) == 2:
                    remfreq1, remfreq2 = totalfreq[chr1] - curd[chr1], totalfreq[chr2] - curd[chr2]
                    if (curd[chr1] == 1 and remfreq2 > 0) or (curd[chr2] == 1 and remfreq1 > 0):
                        break
                    curd[text[i]] -= 1
                    if curd[text[i]] == 0:
                        curd.pop(text[i])
                    i += 1
            res = max(res, j - i + 1)
        return res