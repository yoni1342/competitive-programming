class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.rec([1],rowIndex)
    def rec(self, arr, n):
        if n==0:
            return arr
        
        temp = []
        if len(arr)>1:
            left = 0
            Sum = 0
            for right in range(len(arr)):
                Sum+=arr[right]
                
                if right-left+1 ==2:
                    temp.append(Sum)
                    Sum-=arr[left]
                    left+=1
            return self.rec([1]+temp+[1], n-1)
        else:
            return self.rec([1]+[1], n-1)