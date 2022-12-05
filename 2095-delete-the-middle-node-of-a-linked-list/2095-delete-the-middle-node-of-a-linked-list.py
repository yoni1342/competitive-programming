# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next:
            turtle = head
            rabbit = head
            prev = None

            while rabbit.next:
                if rabbit.next.next == None:
                    rabbit = rabbit.next
                else:
                    rabbit = rabbit.next.next
                prev = turtle
                turtle = turtle.next
            prev.next = turtle.next
        else:
            head = None
        return head
            