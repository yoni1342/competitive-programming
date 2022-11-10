# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        if head.next:
            t = head
            r = head
            while r.next != None:
                if r.next.next == None:
                    r = r.next
                else:
                    r = r.next.next
                t=t.next
            return t
                