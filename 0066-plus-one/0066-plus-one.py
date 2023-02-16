class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = str(int(''.join(map(str,digits)))+1)
        ans = list(map(int, num))
        return ans