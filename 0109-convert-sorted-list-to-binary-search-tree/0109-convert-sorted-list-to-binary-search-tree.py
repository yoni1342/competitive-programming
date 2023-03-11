# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.rec(head)
    
    def rec(self, listNode):
        if not listNode: return
        
        fast = slow = listNode
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        newNode = TreeNode(slow.val)
        
        if prev:
            prev.next = None
            newNode.left = self.rec(listNode)
            newNode.right = self.rec(slow.next)
        else:
            newNode.right = self.rec(slow.next)
        
        
        return newNode