class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        Stack = []
        for i in range(len(temperatures)):
            while Stack and temperatures[Stack[-1]]<temperatures[i]:
                ans[Stack[-1]] = i - Stack[-1]
                Stack.pop()
            Stack.append(i)
        return ans