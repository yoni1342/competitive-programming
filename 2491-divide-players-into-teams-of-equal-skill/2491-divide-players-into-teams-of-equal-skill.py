class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        divide = []
        left = 0
        right = len(skill)-1
        
        while left<right:
            if divide and sum(divide[-1]) != (skill[left]+skill[right]):
                return -1
            divide.append((skill[left], skill[right]))
            left+=1
            right-=1
        print(divide)
        return sum([math.prod(i) for i in divide])