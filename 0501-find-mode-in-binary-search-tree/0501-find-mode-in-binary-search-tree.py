# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        Hash = defaultdict(int)
        
        def rec(curNode):
            if curNode:
                rec(curNode.left)
                Hash[curNode.val]+=1
                rec(curNode.right)
        
        rec(root)
        s = sorted(Hash.items(), key=lambda x: x[1], reverse=True)
        
        ans = []
        
        val = s[0][1]
        
        for i in range(len(s)):
            if s[i][1] == val:
                ans.append(s[i][0])
        
        return ans