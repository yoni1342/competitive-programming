class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-x for x in stones]
        heapify(arr)
        
        while len(arr)>1:
            one = heappop(arr)
            two = heappop(arr)
            smash = one-two
            heappush(arr,smash)
        
        if arr:
            return -arr[0]
        return arr