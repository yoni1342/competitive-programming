# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        self.remove(dummy, val)
        return dummy.next
        
    def remove(self, curNode, val):
        if not curNode:
            return
        if curNode.next and curNode.next.val == val:
            curNode.next = curNode.next.next
            self.remove(curNode,val)        
        self.remove(curNode.next,val)