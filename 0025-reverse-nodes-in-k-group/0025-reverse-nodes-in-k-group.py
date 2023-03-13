# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.dummy = self.dummyPtr = ListNode()
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head:
            ptr = head
            prev = None
            
            for i in range(k):
                prev = ptr
                if not ptr.next and i!=k-1:
                    self.dummyPtr.next = head
                    return self.dummy.next
                elif not ptr.next and i==k-1:
                    self.dummyPtr = self.reverse(head)
                    self.dummyPtr.next = None
                    return self.dummy.next
                ptr = ptr.next
            
            prev.next = None
            self.dummyPtr = self.reverse(head)
            self.dummyPtr.next = None
            head = ptr
            
    def reverse(self, curr):
        if not curr.next:
            self.dummyPtr.next = curr
            return curr
        
        temp = self.reverse(curr.next)
        temp.next = curr
        return curr