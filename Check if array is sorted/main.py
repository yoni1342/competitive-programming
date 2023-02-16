#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tt = int(input())
    while tt > 0:
        tt-=1
        n = int(input())
        a = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(a, n)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends
