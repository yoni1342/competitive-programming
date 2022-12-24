class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        leftPtr = 0
        rightPtr = len(x)-1
        
        while leftPtr<rightPtr:
            if x[leftPtr]!=x[rightPtr]:
                return False
            leftPtr+=1
            rightPtr-=1
        return True