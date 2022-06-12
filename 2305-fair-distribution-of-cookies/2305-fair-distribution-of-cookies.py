class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def DFS(i, child, maxim):
            nonlocal ans
            if i < 0:
                ans = min(ans,maxim)
                return ans

            if ans <= max(child):
                return float("inf")
            
            subans = float("inf")
            for j in range(k):
                child[j] += cookies[i]
                curr = DFS(i - 1, child, max(maxim,child[j]))
                child[j] -= cookies[i]
                subans = min(curr, subans)
            return subans

        n = len(cookies)
        ans = float("inf")
        child = [0]*k
        return DFS(n - 1, child, float("-inf"))