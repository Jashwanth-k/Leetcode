# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr1 = curr2 = helper = head
        for i in range(k-1):
            curr1 = curr1.next
            helper = helper.next
            
        while helper.next:
            curr2 = curr2.next
            helper = helper.next
            
        curr1.val,curr2.val = curr2.val,curr1.val
        return head