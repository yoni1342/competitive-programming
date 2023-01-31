# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        
        while p1:
            while p2 and p1.val == p2.val:
                p2 = p2.next
            p1.next = p2
            p1 = p1.next
        
        return head