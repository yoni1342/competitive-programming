class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [];
        for x in range(1, n+1):
            if (not x%3 and not x%5):
                arr.append("FizzBuzz") 
            elif not x%3:
                arr.append("Fizz")
            elif not x%5:
                arr.append("Buzz")
            else:
                arr.append(str(x))
        return arr