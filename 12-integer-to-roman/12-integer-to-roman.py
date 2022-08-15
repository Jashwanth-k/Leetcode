class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1 : "I",5 : "V",10 : "X",50 : "L",100 : "C",500 : "D",1000 : "M"}
        def helper(n,l):
            if n == "0":
                return ""
            if n == "1":
                nbr = int("1" + "0" * l)
                return d[nbr]
            if n <= "3":
                nbr = int("1" + "0" * l)
                return d[nbr] * int(n[0])
            if n <= "8":
                nbr = int("5" + "0" * l)
                n = int(n + "0" * l)
                subnbr = str(abs(nbr - n))
                newnbr, subl = subnbr[0], len(subnbr)
                lr = helper(newnbr, subl-1)
                return lr + d[nbr] if str(n)[0] <= "5" else d[nbr] + lr
            if n == "9":
                nbr = int("10" + "0" * l)
                n = int(n + "0" * l)
                subnbr = str(abs(nbr - n))
                newnbr, subl = subnbr[0], len(subnbr)
                lr = helper(newnbr,subl-1)
                return lr + d[nbr]
            
        num = str(num)
        m = len(num)
        res = ""
        for i in range(m):
            res += helper(num[i],m-i-1)
        return res