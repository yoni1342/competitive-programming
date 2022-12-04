class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l,Min,minAv=0,0,[]
        prefix = [0]*(len(nums)+1)
#         Create Prefix Sum of the list
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
            
        while l<len(nums):
            if len(nums)-1-l != 0:
                Av = abs((prefix[l+1]//(l+1))-((prefix[-1]-prefix[l+1])//(len(nums)-1-l)))
            else:
                Av = abs(prefix[l+1]//(l+1))
            minAv.append(Av)
            if Av<minAv[Min]:
                Min = l
            l+=1
        return Min