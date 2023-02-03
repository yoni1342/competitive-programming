# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left = list1
        count = 0
        while count<a-1:
            left = left.next
            count+=1
        right = left
        while right and count<b+1:
            right = right.next
            count+=1
        
        left.next = list2
        while left.next:
            left = left.next
        
        left.next = right
        
        return list1