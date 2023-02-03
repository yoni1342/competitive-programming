# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ans_ptr=ListNode(0)
        
        p1 = l1
        p2 = l2
        
        curry = 0
        
        while p1 and p2:
            Sum = p1.val + p2.val + curry
            curry = Sum//10
            ans_ptr.next = ListNode(Sum%10)
            
            ans_ptr = ans_ptr.next
            p1 = p1.next
            p2 = p2.next
        
        if p1:
            while p1:
                Sum = p1.val+curry
                curry = Sum//10
                ans_ptr.next = ListNode(Sum%10)
                
                ans_ptr = ans_ptr.next
                p1 = p1.next
        else:
            while p2:
                Sum = p2.val+curry
                curry = Sum//10
                ans_ptr.next = ListNode(Sum%10)
                
                ans_ptr = ans_ptr.next
                p2 = p2.next
        if curry:
            ans_ptr.next = ListNode(curry)
            ans_ptr = ans_ptr.next
        return ans.next