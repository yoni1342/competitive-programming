class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        if (left==0 or right == 0) or (math.floor(math.log(right,2)) - math.floor(math.log(left,2)))!=0:
            return 0
        
        xor = left^right
        
        count = 0
        while xor != 0:
            xor >>= 1
            count += 1
        
        left >>= count
        left <<= count
        
        return left