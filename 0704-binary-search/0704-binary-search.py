class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0
        avg = None
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        while left<right-1:
            avg = math.ceil((left+right)/2)
            if nums[avg]<target:
                left = avg
            elif nums[avg]>target:
                right = avg
            else:
                return avg
        return -1   