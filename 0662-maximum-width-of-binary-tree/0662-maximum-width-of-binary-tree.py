# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        
        ans = 0
        
        while q:
            ans = max(ans, abs(q[-1][1]-q[0][1]))
            
            for i in range(len(q)):
                node,temp = q.popleft()
            
                if node.left:
                    q.append((node.left, temp * 2 - 1))
                if node.right:
                    q.append((node.right, temp*2))
                    
        return ans+1