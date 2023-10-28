class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = [(nums[i],i) for i in range(len(nums))]
        n.sort()
        p1 = 0
        p2 = len(nums)-1
        
        while p1<p2:
            sum_ = n[p1][0] + n[p2][0]
            
            if sum_ == target:
                return [n[p1][1], n[p2][1]]
            
            elif sum_ < target:
                p1+=1
            else:
                p2-=1