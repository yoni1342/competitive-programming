class Solution:
    def findComplement(self, num: int) -> int:
        final = 1 << int.bit_length(num)
        
        return (final-1) ^ num