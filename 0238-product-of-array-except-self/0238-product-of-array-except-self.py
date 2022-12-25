class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProduct = [1]*(len(nums)+1)
        suffixProduct = [1]*(len(nums)+1)
        answer = []
        
        n=len(nums)
        left = 0
        right = n-1
        
        while left<=n and right>=0:
            prefixProduct[left+1] = prefixProduct[left] * nums[left]
            suffixProduct[left+1] = suffixProduct[left] * nums[right]
            left+=1
            right-=1
        
        for i in range(len(nums)):
            product = prefixProduct[i] * suffixProduct[n-i-1]
            answer.append(product)
        
        return answer