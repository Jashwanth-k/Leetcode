class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        def modifyStr(s):
            ones = s.count("1")
            zeros = s.count("0")
            return ("1"*(zeros-1)) + "0" + ("1"*ones)
            
        for i in range(len(binary)):
            if binary[i] == "0":
                return binary[:i] + modifyStr(binary[i:])
        return binary