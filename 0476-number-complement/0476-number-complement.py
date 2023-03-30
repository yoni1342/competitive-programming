class Solution:
    def findComplement(self, num: int) -> int:
        final = 1 << int.bit_length(num)-1
        
        tester = 1
        
        while tester <= final:
            num ^= tester
            tester <<= 1
        
        return num