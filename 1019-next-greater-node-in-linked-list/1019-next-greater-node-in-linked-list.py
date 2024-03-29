# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans, stack = [], []
        
        count = 0 
        
        while head:
            ans.append(0)
            
            while stack and stack[-1][0]<head.val:
                ans[stack[-1][1]] = head.val
                stack.pop()
            
            stack.append((head.val, count))
            head = head.next
            count+=1
        
        return ans