# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary FROM Employee WHERE salary NOT IN (SELECT MAX(e.salary) FROM Employee as e)