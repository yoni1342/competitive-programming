# Write your MySQL query statement below

select e.name as Employee
From Employee e
Join Employee m ON e.managerId = m.id
WHERE e.salary > m.salary