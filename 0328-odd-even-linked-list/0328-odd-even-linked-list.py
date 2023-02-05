# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = even_ptr = ListNode(0)
        odd = odd_ptr = ListNode(0)
        
        cur = head
        count = 1
        while cur:
            if count%2==0:
                even_ptr.next = cur
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = cur
                odd_ptr = odd_ptr.next
            
            cur= cur.next
            count+=1
        
        
        even_ptr.next = None
        
        odd_ptr.next = even.next
        
        return odd.next