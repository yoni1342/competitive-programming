class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hash = {}
        
        for i in nums:
            if i in Hash:
                Hash[i]+=1
            else:
                Hash[i] = 1
        
        answer = dict(sorted(Hash.items(), key=lambda item:item[1],reverse=True)[:k]) 
        
        return answer