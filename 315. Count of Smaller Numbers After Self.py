class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.count = 0
        self.arr = [0] * len(nums)
        nums = list(enumerate(nums , 0))

        self.mergeSort(nums , 0 , len(nums) - 1)
        return self.arr

    def mergeSort(self , nums , left , right):
        if left == right:
            return [nums[left]]
        mid = left + (right - left) // 2

        left = self.mergeSort(nums , left ,mid)
        right = self.mergeSort(nums , mid + 1 , right)

        return self.merge(left , right)


    def merge(self , left , right):
        i = 0
        j = 0
        while i < len(left):
            while j < len(right) and left[i][1] > right[j][1]:
                j += 1
            self.arr[left[i][0]] += j
            #self.arr[left[i][0]] += 1

                

            i += 1
        i = 0
        j = 0
        ans = []
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        while i < len(left):
            ans.append(left[i])
            i += 1

        while j < len(right):
            ans.append(right[j])
            j += 1

        return ans
