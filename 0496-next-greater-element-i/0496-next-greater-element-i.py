class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            temp = nums2.copy()
            Max = 0
            while(i != temp[-1] and temp[-1]!=temp[0]):
                if i<temp[-1]:
                    Max = temp[-1]
                temp.pop()
            if Max == 0:
                ans.append(-1)
            else:
                ans.append(Max)
        return ans
                