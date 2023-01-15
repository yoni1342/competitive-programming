# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        top, left, right, buttom = 0, 0, n-1, m-1
        
        cur_node = head
        while left < right and top<buttom:
            
            for i in range(left, right):
                if cur_node:
                    matrix[top][i] = cur_node.val
                    cur_node = cur_node.next
            
            for i in range(top, buttom):
                if cur_node:
                    matrix[i][right] = cur_node.val
                    cur_node = cur_node.next
            for i in range(right, left, -1):
                if cur_node:
                    matrix[buttom][i] = cur_node.val
                    cur_node = cur_node.next
            for i in range(buttom, top, -1):
                if cur_node:
                    matrix[i][left] = cur_node.val
                    cur_node = cur_node.next
            left+=1
            right-=1
            top+=1
            buttom-=1
        
        if top==buttom:
            for i in range(left, right+1):
                if cur_node:
                    matrix[top][i] = cur_node.val
                    cur_node = cur_node.next
        if left==right:
            for i in range(top, buttom+1):
                if cur_node:
                    matrix[i][left] = cur_node.val
                    cur_node = cur_node.next
        
        return matrix