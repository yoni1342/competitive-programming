class Solution:
    def average(self, salary: List[int]) -> float:
        sortedSalary = sorted(salary)
        n = len(salary)
        sumOfSalary = 0
        for salaryPtr in range(1, n-1):
            sumOfSalary+=sortedSalary[salaryPtr]
        
        averageSalary = sumOfSalary/(n-2)
        
        return averageSalary
            
        