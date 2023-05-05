class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cord = defaultdict(list)
        cur = defaultdict(int)
        n = len(board)
        count = n*n
        
        right = True if n%2==0 else False
        for i in range(n):
            
            if right:
                for j in range(n):
                    cord[count].append(i)
                    cord[count].append(j)
                    cur[(i,j)] = count
                    count-=1
                right = not right
                continue
            else:
                for j in range(n-1,-1,-1):
                    cord[count].append(i)
                    cord[count].append(j)
                    cur[(i,j)] = count
                    count-=1
                right = not right
                continue
        
        que = deque([1])
        visited = set()
        
        visited.add((n-1,0))
        
        ans = [-1]*(n*n+1)
        ans[1] = 0
        while que:
            
            curr = que.popleft()
            ran = [curr+1, min(curr+6, n*n)+1]
            
            for i in range(ran[0], ran[1]):
                nr,nc = cord[i]
                
                dest = board[nr][nc] if board[nr][nc] != -1 else i
                
                if ans[dest] == -1:
                    ans[dest] = ans[curr]+1
                    que.append(dest)
        
        return ans[n*n]
                