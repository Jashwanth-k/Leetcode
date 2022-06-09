class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = ct = waiting = 0
        for arr,time in customers:
            if arr > waiting:
                waiting = arr + time
                total += time
            else: 
                waiting += time
                total += waiting - arr
            ct += 1
        return total / ct