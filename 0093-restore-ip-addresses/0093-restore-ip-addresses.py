class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = set()
        
        def back(idx, path):
            if path and path[-1][0] == '0'and len(path[-1])>1:
                return
            
            if idx >= len(s) and len(path)==4:
                ans.add('.'.join(path))
            
            for i in range(idx, len(s)):
                
                if int(s[idx:i+1]) <= 255:
                    path.append(s[idx: i+1])
                    back(i+1, path)
                    path.pop()
                    
                else:
                    return
        
        back(0, [])
        return ans