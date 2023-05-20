class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ind = 0

        def partition (low, high):
            
            pivot = nums[high]
            i = low - 1

            for j in range(low,high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i],nums[j] = nums[j],nums[i]
            nums[i + 1],nums[high] = nums[high], nums[i + 1]
            return i + 1
        
        def quick(low,high):
            nonlocal ind
            
            if low > high:
                return
            
            index = partition(low,high)

            if index == len(nums) - k:
                ind = index
            elif index > len(nums) - k:
                quick(low, index - 1)
            elif index < len(nums) - k:
                quick(index + 1, high)
            
        
        quick(0, len(nums) - 1)
        
        return nums[ind]
