class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        path = []
        tester = 0
        
        def back(idx):
            nonlocal tester            
            nonlocal ans
            
            if path and idx % path[-1] != 0 and path[-1]%idx != 0:
                return
            if idx == n:
                ans+=1
                return 
            for i in range(1,n+1):
                if tester & (1 << i) == 0:
                    tester |= 1<<i
                    path.append(i)
                    back(idx+1)
                    path.pop()
                    tester &= ~(1<<i)
        
        back(1)
        return ans