# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        power = 0
        ans = ListNode(0)
        head1,head2,helper = l1,l2,ans
        
        while head1 or head2:
            head1_val = head1.val if head1 else 0
            head2_val = head2.val if head2 else 0
            curr = head1_val + head2_val + power
            helper.next = ListNode(curr % 10)
            power = curr // 10
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
            helper = helper.next
        
        if power: helper.next = ListNode(power)
        return ans.next