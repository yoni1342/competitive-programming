class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        prefix = [0]*(len(nums)+1)
        
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        
        que = deque()
        
        res = float('inf')
        for i in range(len(prefix)):
            
            while que and que[-1][0] - que[0][0] >= k:
                res = min(res, que[-1][1]-que[0][1])
                que.popleft()
            
            while que and que[-1][0] >= prefix[i]:
                que.pop()
            
            que.append((prefix[i], i))
        
        while que and que[-1][0] - que[0][0] >= k:
            res = min(res, que[-1][1]-que[0][1])
            que.popleft()
            
        if res == float('inf'):
            return -1
        
        return res