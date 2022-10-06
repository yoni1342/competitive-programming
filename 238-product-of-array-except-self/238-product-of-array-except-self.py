class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*(len(nums)+1)        
        suffix = [1]*(len(nums)+1)
        
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]*nums[i]
            suffix[i+1] = suffix[i]*nums[len(nums)-1-i]
        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i]*suffix[len(suffix)-2-i])
        return answer