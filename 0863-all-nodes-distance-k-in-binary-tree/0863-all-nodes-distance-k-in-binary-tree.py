# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = defaultdict(list)
        ans = []
        visited = set()
        visited.add(target.val)
        def rec(node):
            nonlocal d
            if node:
                if node.left:
                    d[node.left.val].append(node.val)
                    d[node.val].append(node.left.val)                    
                if node.right:
                    d[node.right.val].append(node.val)
                    d[node.val].append(node.right.val)                    
                rec(node.left)
                rec(node.right)
        rec(root)
       
        def helper(arr, k):
            nonlocal ans
            nonlocal visited
            if k == 1:
                for i in range(len(arr)):
                    if arr[i] not in visited:
                        ans.append(arr[i])
            else:
                print(arr)
                for i in arr:
                    if i not in visited:
                        visited.add(i)
                        helper(d[i], k-1)
        
        # print(target)
        if k == 0:
            ans.append(target.val)
        else:
            helper(d[target.val], k)
        return ans