class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        final = 0
        prefix = [0]*(len(arr)+1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i]+arr[i]
        while left<=len(arr)-k:
            if((prefix[left+k]-prefix[left])/k>=threshold):
                final+=1
            left+=1
        return final