class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        left = 0
        right = n-k
        
        traveled = set()
        
        while right<n:
            temp = nums[left]
            nums[left] = nums[right]
            traveled.add(left)
            
            j = left+k%n
            while j not in traveled:
                temp, nums[j] = nums[j], temp
                traveled.add(j)
                j = (j+k)%n
            
            if len(traveled)!=n:
                while left < n and left in traveled:
                    left+=1
                while right < n and right in traveled:
                    right+=1
            else:
                break