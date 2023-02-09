class Solution:
    def __init__(self):
        self.ans = 0
    def distinctNames(self, ideas: List[str]) -> int:
        prefix = defaultdict(set)
        suffix = defaultdict(set)    
        visited = set()
        
        ans = set()
        
        for i in ideas:
            prefix[i[1:]].add(i[:1])
            suffix[i[:1]].add(i[1:])
        
        for i in suffix: #O(26)
            for j in prefix.values(): #O(n)
                if i not in j:
                    for k in j: #O(26)
                        if k+i not in visited and i+k not in visited:
                            self.comb(suffix[k], suffix[i])
                            visited.add(i+k)
                            visited.add(k+i)
        return self.ans

    def comb(self, s1, s2):
        intersection = len(s1 & s2)
        self.ans += 2*( len(s1)-intersection)*(len(s2)-intersection)
        