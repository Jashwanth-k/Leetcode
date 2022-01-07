import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
        return count
    
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.len = self.length(self.head)
        
    def getNode(self,head,idx):
        curr = head
        while idx != 0:
            idx -= 1
            curr = curr.next
        return curr.val
            
    def getRandom(self) -> int:
        idx = random.randint(0,self.len-1)
        return self.getNode(self.head,idx)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()