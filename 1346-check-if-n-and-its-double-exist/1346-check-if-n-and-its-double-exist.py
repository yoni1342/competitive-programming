class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
#        we can use set coz set holds unique data 
        s =  set()
        
        for num in arr:
            if num*2 in s or num/2 in s:
                return True
            s.add(num)
            
        return False