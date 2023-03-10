# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rec(root, 0)
        return self.ans
    def rec(self, curNode, k):
        l = len(self.ans)
        if not curNode:
            return 
    
        if k<l:
            self.ans[k] = curNode.val
        else:
            self.ans.append(curNode.val)
        
        self.rec(curNode.left, k+1)
        self.rec(curNode.right, k+1)