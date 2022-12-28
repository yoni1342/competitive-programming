class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winHash = {}
        lossHash = {}
        answer = [[],[]]
        for win,loss in matches:
            if win in winHash:
                winHash[win] +=1
            else:
                winHash[win] = 1
            if loss in lossHash:
                lossHash[loss] +=1
            else:
                lossHash[loss] = 1
        
        for i in winHash:
            if i not in lossHash:
                answer[0].append(i)
        for key,value in lossHash.items():
            if value == 1:
                answer[1].append(key)
        
        answer[0].sort()        
        answer[1].sort()

        return answer