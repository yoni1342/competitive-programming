# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        cur = head
        
        while cur:
            n+=1
            cur = cur.next
        
        ans = [0]*(n)
        
        index = 0
        cur = head
        stack = []
        
        while cur:
            
            while stack and stack[-1][0]<cur.val:
                ans[stack[-1][1]] = cur.val
                stack.pop()
                
            if not stack or cur.val<=stack[-1][0]:
                stack.append((cur.val, index))
            
            cur = cur.next
            index+=1
        
        return ans