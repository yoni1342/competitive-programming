# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        rev = None
        slow,fast = head,head
        
        while fast and fast.next:
            fast = fast.next.next
            rev,rev.next,slow = slow,rev,slow.next
        
        Max = 0
        while rev and slow:
            Max = max(Max, rev.val+slow.val)
            rev = rev.next
            slow = slow.next
        
        return Max