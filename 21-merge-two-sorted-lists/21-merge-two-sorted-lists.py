# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        fh = ft = None
        if list1.val < list2.val:
            fh = ft = list1
            list1 = list1.next
        else:
            fh = ft = list2
            list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ft.next = list1
                ft = ft.next
                list1 = list1.next
            else:
                ft.next = list2
                ft = ft.next
                list2 = list2.next

        if list1 is not None:
            ft.next = list1
        else:
            ft.next = list2

        return fh