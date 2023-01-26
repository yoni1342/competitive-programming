class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n-1
        
        ans = 0
        
        while left<=right:
            if people[right]+people[left]<=limit:
                ans+=1
                left+=1
                right-=1
            else:
                ans+=1
                right-=1
        return ans