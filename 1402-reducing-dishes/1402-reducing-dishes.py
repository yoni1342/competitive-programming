class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        total = 0
        cur_sum = 0
        
        for i in satisfaction:
            cur_sum += i
            
            if cur_sum < 0:
                break
            total += cur_sum
        
        return total    