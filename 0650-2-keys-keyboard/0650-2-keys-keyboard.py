class Solution:
    def minSteps(self, n: int) -> int:
        cur = 1
        count = 0
        buffer = 0

        while cur < n:
            rem = n-cur

            if rem % cur == 0:
                buffer = cur
                cur += buffer
                count += 2
            else:
                cur += buffer
                count += 1
        
        return count