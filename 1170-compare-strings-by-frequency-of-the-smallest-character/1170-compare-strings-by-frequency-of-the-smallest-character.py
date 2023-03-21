class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            Hash=defaultdict(int)
            for  i in s:
                Hash[ord(i)]+=1
            
            return Hash[min(Hash)]
        
        a = [f(x) for  x in words]
        a.sort()
        
        def bs(target):
            l = -1
            r = len(a)
            
            while l+1 < r:
                mid = (l+r)//2
                
                if a[mid] > target:
                    r = mid
                else:
                    l = mid
                    
            return len(a)-r
        
        ans = []
        for i in queries:
            ans.append( bs(f(i)))
        
        return ans
                    