class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        d = collections.defaultdict(int)
        maxim = 0
        ans = ""
        for i in range(n):
            message,sender = messages[i],senders[i]
            d[sender] += len(message.split())
            maxim = max(maxim,d[sender])
            
        for i in d:
            if d[i] == maxim:
                ans = max(ans,i)
        return ans