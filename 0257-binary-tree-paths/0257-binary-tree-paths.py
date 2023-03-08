# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs(root, "")
        return self.ans
    
    def dfs(self,curNode, path):
        if not curNode.left and not curNode.right:
            self.ans.append(path+str(curNode.val))
        
        if curNode.left:
            left = self.dfs(curNode.left, path+str(curNode.val)+"->")
        if curNode.right:
            right = self.dfs(curNode.right, path+str(curNode.val)+"->")
        
        return