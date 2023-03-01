class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        scor = self.predict(nums, 0, len(nums)-1, True)
        return scor[0]>=scor[1]
        
    def predict(self, arr, left, right, p1Turn):
        # base case
        if left == right:
            if p1Turn:
                return [arr[left],0]
            else:
                return [0,arr[left]]
        
        if p1Turn:
            r = self.predict(arr, left, right-1, not p1Turn)
            r[0]+=arr[right]
            l = self.predict(arr, left+1, right, not p1Turn)
            l[0]+=arr[left]
            
            if r[0]>=l[0]:
                return r
            return l
        else:
            r = self.predict(arr, left, right-1, not p1Turn)
            r[1]+=arr[right]
            l = self.predict(arr, left+1, right, not p1Turn)
            l[1]+=arr[left]
            
            if r[1]>=l[1]:
                return r
            return l
    