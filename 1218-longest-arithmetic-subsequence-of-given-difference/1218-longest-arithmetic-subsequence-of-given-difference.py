class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = defaultdict(int)
                
        for i in range(len(arr) -1 ,-1,-1):
            memo[arr[i]] = memo[arr[i]+difference]+1 
            
        
        return max(memo.values())
    