class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        max_ = max(count.values())
        ans = [[] for _ in range(max_)]
        nums.sort()
        
        for i in nums:
            for j in ans:
                if i not in j:
                    j.append(i)
                    break
        
        return ans
        