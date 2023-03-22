class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Max = deque()
        que = deque()
        
        res = []
        
        l = 0
        for r in range(len(nums)):
            
            if r - l + 1 <= k:
                
                while que and que[-1] < nums[r]:
                    que.pop()
                
                que.append(nums[r])
                        
            
            if r-l+1 == k:

                # append on res
                res.append(que[0])
                
                # cheke if the the nums[l] is nums[0]    
                if nums[l] == que[0]:
                    que.popleft()

                l+=1
        return res