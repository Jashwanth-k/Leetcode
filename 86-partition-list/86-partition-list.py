# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode(-1)
        c1 = head1
        head2 = ListNode(-1)
        c2 = head2
        curr = head
        while curr:
            if curr.val < x:
                c1.next = ListNode(curr.val)
                c1 = c1.next
            else:
                c2.next = ListNode(curr.val)
                c2 = c2.next
            curr = curr.next
        c1.next = head2.next
        return head1.next