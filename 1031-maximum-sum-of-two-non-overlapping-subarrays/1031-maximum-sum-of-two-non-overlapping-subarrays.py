class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        l = 0
         #[8,20,6,2,20,17,6,3,20,8,12]
        Sum = 0
        n= len(nums)
        while(l<=n-firstLen):
            r=0
            leftSum = sum(nums[l:l+firstLen])
            while(r<=len(nums)-secondLen):
                if l+firstLen-1<r or r+secondLen-1<l:
                    rightSum= sum(nums[r:r+secondLen])
                    Sum = max(Sum, leftSum+rightSum)
                r+=1
            l+=1
        return Sum
                