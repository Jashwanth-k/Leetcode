# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        helper = []
        if head is None:
            return head
        while head:
            helper.append(head.val)
            head = head.next
        
        k = k % len(helper)
        idx = len(helper)-k
        helper = helper[idx:] + helper[:idx]
        
        temp = ListNode(0)
        curr = temp
        for i in helper:
            curr.next = ListNode(i)
            curr = curr.next
        return temp.next
        