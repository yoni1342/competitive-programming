# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        even = not fast
        
        prev = slow
        cur = slow.next
        
        while cur:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        
        right = prev
        left = head
        
        if even:
            while left.next!=right:
                if left.val != right.val:
                    return False
                left = left.next
                right = right.next
            if left.val == right.val:
                return True
            return False
        else:
            while left != right:
                if left.val != right.val:
                    return False
                left = left.next
                right = right.next
            return True
        