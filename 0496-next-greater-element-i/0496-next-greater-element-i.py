class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         1st Try
        """
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
        """
#lets try to optimize it using hashmap and monotonic-stack
        
        stack = []
        ans = []
        Hash = {}
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                j = stack.pop()
                Hash[nums2[j]] = nums2[i]
            stack.append(i)
        for i in nums1:
            if i not in Hash:
                ans.append(-1)
            else:
                ans.append(Hash[i])
        return ans
            
                