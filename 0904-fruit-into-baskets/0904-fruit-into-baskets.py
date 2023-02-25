class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        Hash = defaultdict(int)
        left = 0
        res = 0
        
        for right in range(len(fruits)):
            Hash[fruits[right]]+=1
        
            while len(Hash)>2:
                Hash[fruits[left]]-=1
                if Hash[fruits[left]] == 0:
                    del Hash[fruits[left]]
                left+=1
            res = max(res, (right-left)+1)
        
        return res
    