class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dp=Counter(nums)
        list1 = []
        for key,val in dp.items():
            if val==2:
                list1.append(key)
        
        return list1
