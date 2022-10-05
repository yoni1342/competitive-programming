class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k%len(nums)
        l, r, cur = 0, k, nums[0]
        swap, n = 0, len(nums)
        unique = set()
        while swap<n:
            if r not in unique:
                unique.add(r)
                if r < n:
                    nums[r], cur = cur, nums[r]
                l=r
                r=r+k
                if r>=n:
                    r-=n
                swap+=1
            else:
                l+=1
                if l>n:
                    l-=n
                cur = nums[l]
                r=l+k
                if r>=n:
                    r-=n