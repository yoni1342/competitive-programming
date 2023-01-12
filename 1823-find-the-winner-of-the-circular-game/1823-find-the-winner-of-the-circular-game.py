class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1,n+1)]
        unique = set()
        i = 0 
        
        while len(unique) < n-1:
            if nums[i%n] not in unique:
                c = 0
                while c!=k:
                    if nums[i%n] not in unique:
                        c+=1
                    if c!=k:
                        i+=1
                unique.add(nums[i%n])
            i+=1
            
        winner = [ i for i in set(nums).difference(unique)]
        return winner[0]