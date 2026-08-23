# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        newList=ListNode()
        dummy=newList
        while l1 is not None or l2 is not None:
            if l2 is None:
                dummy.next=ListNode(l1.val)
                l1=l1.next
                dummy=dummy.next
            elif l1 is None:
                dummy.next=ListNode(l2.val)
                l2=l2.next
                dummy=dummy.next
            else:
                if l1.val==l2.val:
                    dummy.next=ListNode(l1.val)
                    dummy=dummy.next
                    dummy.next=ListNode(l2.val)
                    dummy=dummy.next
                    l1=l1.next
                    l2=l2.next
                
                elif l1.val < l2.val:
                    dummy.next=ListNode(l1.val)
                    dummy=dummy.next
                    l1=l1.next
                else:
                    dummy.next=ListNode(l2.val)
                    dummy=dummy.next
                    l2=l2.next
        return newList.next

