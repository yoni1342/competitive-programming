# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ans_ptr = ListNode(0)
        
        p1 = list1
        p2 = list2
        
        while p1 and p2:
            if p1.val<p2.val:
                ans_ptr.next = p1
                ans_ptr = ans_ptr.next
                p1 = p1.next
            elif p2.val<p1.val:
                ans_ptr.next = p2
                ans_ptr = ans_ptr.next
                p2 = p2.next
            elif p2.val == p1.val:
                ans_ptr.next = p2
                ans_ptr = ans_ptr.next
                p2 = p2.next
                
                ans_ptr.next = p1
                ans_ptr = ans_ptr.next
                p1 = p1.next

        if p1:
            ans_ptr.next = p1
        elif p2:
            ans_ptr.next = p2

        
        return ans.next