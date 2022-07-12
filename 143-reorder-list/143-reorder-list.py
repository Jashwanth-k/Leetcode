# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None: return
        slow = head
        fast = head.next
        while slow and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        prev,curr,nxt = None,mid,mid.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt: nxt = nxt.next
        head2 = prev
        head1 = head
    
        while head1:
            nxt1 = head1.next
            nxt2 = head2.next
            head1.next = head2
            if not nxt1: break
            head2.next = nxt1
            head1 = nxt1
            head2 = nxt2