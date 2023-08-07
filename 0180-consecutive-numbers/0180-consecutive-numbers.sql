SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num, LEAD(num) OVER (ORDER BY id) as next_num,
           LEAD(num, 2) OVER (ORDER BY id) as next_next_num
    FROM Logs
) AS subquery
WHERE num = next_num AND num = next_next_num;