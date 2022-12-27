class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ptr = 0
        n = len(arr)
        
        while ptr < n:
            if arr[ptr] == 0:
                arr.pop()
                arr.insert(ptr, 0)
                ptr+=1
            ptr+=1
                    