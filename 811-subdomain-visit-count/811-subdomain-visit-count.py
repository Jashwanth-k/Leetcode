class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = collections.defaultdict(int)
        for domains in cpdomains:
            idx = domains.index(" ")
            currDomain = domains[idx+1:].split(".")
            freq = int(domains[:idx])
            for i in range(len(currDomain)):
                d[".".join(currDomain[i:])] += freq
        
        output = []
        for i in d:
            output.append(str(d[i]) + " " + i)
        return output