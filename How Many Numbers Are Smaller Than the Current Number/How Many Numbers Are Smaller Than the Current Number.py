class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNum = sorted(nums)
        Hash = {}
        same = -1
        counter = 0
        
        for i in sortedNum:
            if i!=same:
                Hash[i] = counter
                same = i
                counter+=1
            else:
                counter+=1
                
        return [Hash[i] for i in nums]
