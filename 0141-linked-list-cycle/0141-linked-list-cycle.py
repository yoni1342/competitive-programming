# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        unique = set()
        
        while cur:
            if cur in unique:
                return True
            unique.add(cur)
            cur = cur.next
        return False