# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode(0)
        dummy=node
        ll1=l1
        ll2=l2
        s=0
        carry=False
        while ll1 or ll2 or carry:
            v1=ll1.val if ll1 else 0
            v2=ll2.val if ll2 else 0
            s= v1 + v2
            if carry:
                s+=1
                carry=False    
           
            if  s >= 10:
                r=s%10
                dummy.next=ListNode(r)
                carry=True
            else:
                dummy.next=ListNode(s)
            dummy=dummy.next
            ll1=ll1.next if ll1 else None
            ll2=ll2.next if ll2 else None
        
        return node.next
        