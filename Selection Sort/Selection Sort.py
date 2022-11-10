class Solution: 
    def select(self, arr, i):
        # code here 
        Min = i
        while i<n:
            if arr[i]<arr[Min]:
                Min = i
            i+=1
        return Min
    def selectionSort(self, arr,n):
        #code here
        l =0 
        while l<n:
            Minn = self.select(arr, l)
            arr[Minn],arr[l] = arr[l],arr[Minn] 
            l+=1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends