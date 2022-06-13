class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def DFS(i):
            if i < 0:
                if all(s == square[0] for s in square):
                    return True
                return False
            
            seen = set()
            for j in range(4):
                if square[j] in seen: continue
                if square[j] + matchsticks[i] > self.target: continue
                seen.add(square[j])
                square[j] += matchsticks[i]
                if DFS(i-1):
                    return True
                square[j] -= matchsticks[i]
                
        self.tsum = sum(matchsticks)
        if self.tsum % 4 != 0: return False
        self.target = self.tsum // 4
        square = [0] * 4
        return DFS(len(matchsticks)-1)