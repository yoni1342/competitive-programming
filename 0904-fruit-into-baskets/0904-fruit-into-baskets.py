class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        Hash = defaultdict(int)
        left = 0
        right = 0
        ans = 0
        while right<len(fruits):
            while right<len(fruits) and len(Hash)<=2:
                Hash[fruits[right]]+=1
                right+=1
            
            if len(Hash)>2:
                ans = max(ans, right-left-1)
                
                while len(Hash)>2:
                    Hash[fruits[left]]-=1
                    if Hash[fruits[left]]==0:
                        del Hash[fruits[left]]
                    left+=1
            else:
                ans = max(ans, right-left)

        return ans