class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
#         first we Hash nums 
        Hash = Counter(nums)
        
#       then we calculate the sum of reptetion of the duplicated items using k*(k-1)/2
        
        for i in Hash.values():
            answer += (i*(i-1))//2
        
        return answer
