class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        Int = list(map(int, nums))
        Int.sort()
        print(Int)
        return str(Int[len(Int)-k])