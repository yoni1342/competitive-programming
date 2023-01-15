class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        n = rows-1
        m = cols-1
                
        left,top,right, buttom = cStart, rStart, cStart+1 ,rStart+1
        
        if buttom>n:
            buttom = n
        if right>m:
            right=m
        print(top, left, right, buttom)
        
        ans = []
        visited = set()
        
        if left == 0 and right==0 and top ==0 and buttom==0:
            ans.append([0,0])

        for _ in range(cols+rows):
            
            # setp-1 traverse from top-left corner to top-right corner
            for i in range(left, right):
                if (top,i) not in visited:
                    ans.append([top,i])
                    visited.add((top,i))
            
            # move left pointer one step back
            if left>0:
                left-=1
            
            # step-2 traverse from top-right corner to buttom-right corner
            for i in range(top,buttom):
                if (i,right) not in visited:
                    ans.append([i, right])
                    visited.add((i, right))
            
            # move top pointer one step back
            if top>0:
                top-=1
            
            # step-3 traverse from buttom-right corner to buttom-left corner
            for i in range(right, left, -1):
                if (buttom,i) not in visited:
                    ans.append([buttom, i])
                    visited.add((buttom, i))
            # move right pointer one step
            if right<m:
                right+=1
            
            # step-4 traverse from buttom-left corner to top-left cotner
            for i in range(buttom, top,-1):
                if (i,left) not in visited:
                    ans.append([i, left])
                    visited.add((i,left))
            # move buttom pointer one step
            if buttom<n:
                buttom+=1
        return ans