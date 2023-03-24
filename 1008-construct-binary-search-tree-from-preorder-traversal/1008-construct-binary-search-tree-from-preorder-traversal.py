# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dummy = TreeNode()
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        for i in range(1,len(preorder)):
            self.BST(TreeNode(preorder[i]), root)
        
        return root
    
    def BST(self,node, root):
        
        if not root:
            return node
        if node.val < root.val:
            root.left = self.BST(node,root.left)
            return root
        else:
            root.right = self.BST(node,root.right)
            return root
