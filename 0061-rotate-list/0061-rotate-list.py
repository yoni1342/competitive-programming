# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        n = 0
        p = head
        while p:
            n+=1
            p = p.next
        k = k%n
        p1 = head
        p2 = head
        
        if not p1:
            return head
        for _ in range(k):
            p2 = p2.next
            if not p2:
                p2 = head
        
        while p2.next:
            p2 = p2.next
            p1 = p1.next
            
        if p1==p2:
            return head
        temp = p1.next
        p1.next = None
        p2.next = head
        head = temp
    
        return head