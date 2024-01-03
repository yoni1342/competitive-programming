class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        count = []
        
        for i in bank:
            c = Counter(i)
            
            if '1' in c:
                count.append(c['1'])
            else:
                count.append(0)
        
        temp = 0
        for i in count:
            if i != 0:
                if temp != 0:
                    ans += (temp * i)
                temp = i
        
        return ans