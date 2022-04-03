class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currMin = 60 * int(current[:2]) + int(current[3:])
        corrMin = 60 * int(correct[:2]) + int(correct[3:])
        differ = corrMin - currMin
        oper = 0
        
        for i in [60,15,5,1]:
            oper += differ // i
            differ = differ % i
        return oper