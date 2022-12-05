# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=right=prev=head
        for i in range(n-1):
            right = right.next
        while right.next:
            prev = left
            left = left.next
            right = right.next
        if prev==head and left==head:
            head = left.next
        else:
            prev.next = left.next
        return head