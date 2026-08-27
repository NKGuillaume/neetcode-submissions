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
        while ll1 and ll2:
            s=ll1.val +ll2.val
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
            ll1=ll1.next
            ll2=ll2.next
        while ll1 or ll2:
            if ll1:
                if carry:
                    s=1+ll1.val
                    carry=False
                else:
                    s=ll1.val
                dummy.next=ListNode(s%10)
                ll1=ll1.next
            elif ll2:
                if carry:
                    s=1+ll2.val
                else:
                    s=ll2.val
                dummy.next=ListNode(s%10)
                ll2=ll2.next        
            if s >= 10:
                carry=True
            dummy=dummy.next
        if carry and ll2 is None and ll1 is None:
                print("come here")
                dummy.next=ListNode(1)
        return node.next
        