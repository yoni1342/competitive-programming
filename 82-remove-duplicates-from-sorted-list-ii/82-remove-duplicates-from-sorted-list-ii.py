# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head
        right = None
        if left:
            right = left.next
            prev = None
        while right:
            if right.val!=left.val:
                prev = left
                left = right
                right = right.next
            else:
                while right and right.val==left.val:
                    right = right.next
                if prev == None:
                    head = right
                    left = head
                    if right:
                        right=right.next
                else:
                    prev.next=right
                    left=right
                    if right:
                        right=right.next
        return head