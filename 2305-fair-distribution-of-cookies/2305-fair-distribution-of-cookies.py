class Solution:
    def __init__(self):
        self.ans = float('inf')
        
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        cookies.sort(reverse = True)
        self.backtrack(0, cookies, bucket)
        return self.ans
    def backtrack(self, idx, cookies,bucket):
        if idx >= len(cookies):
            self.ans = min(self.ans, max(bucket))
            return
        if  self.ans <= max(bucket):
            return 
        
        for i in range(len(bucket)):
            bucket[i] += cookies[idx]
            self.backtrack(idx+1,cookies,bucket)
            bucket[i]-= cookies[idx]
        