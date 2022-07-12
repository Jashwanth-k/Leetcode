# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def createRev(head):
            nonlocal helper
            curr = head
            while curr:
                helper.append(curr.val)
                curr = curr.next
            return 
        
        helper = []
        createRev(head)
        n = len(helper)
        c1,n1 = head,head.next
        for i in range(n // 2):
            present = ListNode(helper[n-1-i])
            c1.next = present
            present.next = n1
            c1 = n1
            n1 = n1.next
            
        if n % 2 != 0:c1.next = None
        else: present.next = None