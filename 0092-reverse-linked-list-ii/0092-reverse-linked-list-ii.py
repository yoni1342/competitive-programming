# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        lPrev,cur = dummy, head
        
        for i in range(left-1):
            lPrev,cur = cur, cur.next
        
        prev = None
        temp = cur
        for i in range((right-left)+1):
            t = temp.next
            temp.next = prev
            prev = temp
            temp = t
        lPrev.next.next = temp
        lPrev.next = prev
        return dummy.next