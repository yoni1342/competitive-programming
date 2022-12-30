class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumOfEven = 0
        answer = []
        
        # add all even numbers inside nums array
        for num in nums:
            if num%2 == 0:
                sumOfEven+=num
        
        #itrate over queries and modifiy answer
        for val, index in queries:
            # if both are even
            if val%2 == 0 and nums[index]%2 == 0:
                nums[index]+=val
                sumOfEven += val
                answer.append(sumOfEven)
            # if both are odd
            elif val%2 != 0 and nums[index]%2 != 0:
                nums[index]+=val
                sumOfEven += nums[index]
                answer.append(sumOfEven)
            # if the value from queries is odd and nums[index] is even
            elif val%2!=0 and nums[index]%2 == 0:
                sumOfEven -= nums[index]
                nums[index]+=val
                answer.append(sumOfEven)
            # if nums[index] is odd and value from queries is odd
            else:
                nums[index]+=val
                answer.append(sumOfEven)
        
        return answer
                