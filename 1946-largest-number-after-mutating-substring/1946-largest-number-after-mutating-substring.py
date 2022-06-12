class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        helper = [int(i) for i in num]
        changed = False
        for j in range(len(helper)):
            if (not changed and helper[j] < change[helper[j]]) or (changed and helper[j] <= change[helper[j]]):
                helper[j] = change[helper[j]]
                changed = True
            elif changed:
                break
        ans = ""
        for i in helper:
            ans += str(i)
        return ans