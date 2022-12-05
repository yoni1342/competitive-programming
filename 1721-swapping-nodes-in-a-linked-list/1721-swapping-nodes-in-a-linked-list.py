# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left=right=end=head
        for i in range(k-1):
            left = left.next
            end = end.next
        while end.next:
            end = end.next
            right = right.next
        left.val, right.val = right.val,left.val
        return head