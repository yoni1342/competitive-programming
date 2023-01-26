class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        
        left = 0
        right = len(height)-1
        
        while left<right:
            minheight = min(height[left], height[right])
            area = max(area,((right-left) * minheight))
            
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return area
            