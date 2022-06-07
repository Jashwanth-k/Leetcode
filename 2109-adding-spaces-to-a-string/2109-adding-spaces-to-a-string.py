class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        ans = []
        spaces = collections.deque(spaces)
        for i in range(n):
            if spaces and i == spaces[0]:
                spaces.popleft()
                ans.append(" " + s[i])
            else:
                ans.append(s[i])
        return "".join(ans)