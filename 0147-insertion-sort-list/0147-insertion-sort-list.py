# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while cur.next:
            while cur.next and cur.val<= cur.next.val:
                cur = cur.next
            if cur.next:
                temp = cur.next
                cur.next = cur.next.next

                if temp.val<head.val:
                    temp.next = head
                    head = temp
                else:
                    prev = head
                    Next = head.next

                    while Next.val<temp.val:
                        Next = Next.next
                        prev = prev.next

                    temp.next = Next
                    prev.next = temp
        
        return head
            