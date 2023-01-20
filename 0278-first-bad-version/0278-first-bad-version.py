# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        if isBadVersion(left):
            return left
        if isBadVersion(right) and not isBadVersion(right-1):
            return right
        avg = 0
        
        while left<right-1:
            avg = (left+right)//2
            if isBadVersion(avg) and isBadVersion(avg-1):
                right = avg
            elif isBadVersion(avg) and not isBadVersion(avg-1):
                return avg
                break
            else:
                left = avg
            