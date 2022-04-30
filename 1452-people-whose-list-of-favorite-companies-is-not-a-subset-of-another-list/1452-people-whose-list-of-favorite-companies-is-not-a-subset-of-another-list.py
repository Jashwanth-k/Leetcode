class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        d = [{} for j in range(n)]
        for i in range(n):
            for j in favoriteCompanies[i]:
                d[i][j] = True
            
        output = []
        for i in range(n):
            check = True
            for j in range(n):
                mainlen = len(d[i])
                currlen = len(d[j])
                if i == j or mainlen > currlen:
                    continue
                for k in favoriteCompanies[i]:
                    if k in d[j]:
                        mainlen -= 1
                        if mainlen == 0:
                            check = False
                            break
            if check : output.append(i)
        return output