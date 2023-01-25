class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        t = n-1
        while t>0:
            i=0
            Max = i
            while i<=t:
                if arr[i]>arr[Max]:
                    Max = i
                i+=1
            ans.append(Max+1)
            j = 0
            while j<Max:
                arr[j],arr[Max] = arr[Max],arr[j]
                j+=1
                Max-=1
            ans.append(t+1)
            arr = arr[t::-1]+arr[t+1:]
            
            t-=1
        
        return ans