class Solution:
    def calPoints(self, ops: List[str]) -> int:
        output = []
        for i in ops:
            if i == "C":
                output.pop()
            elif i == "D":
                output.append(output[-1]*2)
            elif i == "+":
                output.append(output[-2] + output[-1])
            else:
                output.append(int(i))
        return sum(output)