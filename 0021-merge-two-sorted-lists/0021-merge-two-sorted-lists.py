# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        self.rec(list1, list2, dummy)
        return dummy.next
    
    def rec(self, N1, N2, dummy):
        # base case
        if not N1 and not N2:
            return dummy
        elif not N1:
            dummy.next = N2
            self.rec(N1, N2.next, dummy.next)
        elif not N2:
            dummy.next = N1
            self.rec(N1.next,N2, dummy.next)
        elif  not N2 or N1.val <= N2.val:
            dummy.next = N1
            self.rec(N1.next,N2, dummy.next)
        elif not N1 or N2.val<N1.val:
            dummy.next = N2
            self.rec(N1, N2.next, dummy.next)
            