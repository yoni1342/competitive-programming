class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        leftOperations = [0]*len(boxes)
        rightOperations = [0]*len(boxes)
        leftCount = 0
        rightCount = 0
        
        # perform left operations
        for index,val in enumerate(boxes):
            if index == 0:
                leftOperations[index] = 0
                if val == '1':
                    leftCount+=1
            elif val == "1":
                leftOperations[index] = leftOperations[index-1]+leftCount
                leftCount+=1
            else:
                leftOperations[index] = leftOperations[index-1]+leftCount
        
        # performing right operations
        
        for index, val in reversed(list(enumerate(boxes))):
            if index == len(boxes)-1:
                rightOperations[index] = 0
                if val == '1':
                    rightCount+=1
            elif val == '1':
                rightOperations[index] = rightOperations[index+1] + rightCount
                rightCount+=1
            else:
                rightOperations[index] = rightOperations[index+1]+rightCount
        
        # finally add leftOperations and rightOperations
        
        answer = [0]*len(boxes)
        for i in range(len(boxes)):
            answer[i] = leftOperations[i]+rightOperations[i]
        
        return answer