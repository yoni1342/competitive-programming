# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.rec(nums)
    
    def rec(self, arr):
        if not arr:
            return
        
        if len(arr)  == 1:
            return TreeNode(arr[0])
        
        mid = len(arr) // 2
        
        newNode = TreeNode(arr[mid])
        newNode.left = self.rec(arr[:mid])
        newNode.right = self.rec(arr[mid+1:])
        
        return newNode