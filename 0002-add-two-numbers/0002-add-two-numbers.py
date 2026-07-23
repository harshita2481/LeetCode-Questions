# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dummynode=ListNode(-1)
        curr=dummynode
        t1=l1
        t2=l2
        carry=0
        while t1 or t2:
            total=carry
            if t1:
                total+=t1.val
            if t2:
                total+=t2.val
            newnode=ListNode(total%10)
            curr.next=newnode
            curr=curr.next
            carry=total//10
            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
        if carry:
            newnode=ListNode(carry)
            curr.next=newnode
        return dummynode.next

        