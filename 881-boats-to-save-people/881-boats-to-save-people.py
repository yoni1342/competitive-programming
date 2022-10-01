class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        i=0
        j= len(people)-1
        
        people.sort()
        while i<=j:
            if people[i]+people[j]<=limit:
                boat+=1
                i+=1
                j-=1
            elif people[i] == limit:
                boat+=1
                i+=1
            elif people[j] == limit:
                boat+=1
                j-=1
            elif people[i]+people[j]>limit:
                boat+=1
                j-=1
            else:
                boat+=1
                i+=1
        return boat
    