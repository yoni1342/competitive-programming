class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*(len(boxes))
        
        ptr = 0
        while ptr<len(boxes):
            c = 0
            while c<len(boxes):
                if boxes[c] == '1':
                    ans[ptr] += abs(ptr-c)
                c+=1
            ptr+=1
        
        return ans