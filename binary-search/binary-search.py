class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        
        lo = 0
        hi = len(nums)-1
        
        while lo <= hi:
            mid = lo+(hi-lo)//2
            
            if nums[mid]>target:
                hi = mid-1
            elif nums[mid]<target:
                lo = mid+1
            else:
                ans = mid
                break
        return ans