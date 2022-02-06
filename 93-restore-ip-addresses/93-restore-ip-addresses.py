class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def helper(s,output,idx = 0,pt = 0):
            splitted = s.split('.')
            if len(splitted) == 4:
                for i in splitted:
                    if i == '':
                        return
                    if int(i) > 255 or int(i) < 0:
                        return
                    if int(i) > 0 and i[0] == "0":
                        return
                    if int(i) == 0 and len(i) != 1:
                        return
                output.append(s)

            if len(splitted) > 4:
                return

            for sp in range(idx+1,len(s)):
                helper(s[:sp+pt] + '.' + s[sp+pt:],output,sp,pt+1)
        
        output = []
        helper(s,output)
        return output