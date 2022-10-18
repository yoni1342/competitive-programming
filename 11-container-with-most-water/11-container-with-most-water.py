class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        MaxArea = 0
        
        while left<right:
            MaxArea = max(MaxArea, (right-left)*min(height[left], height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return MaxArea
                