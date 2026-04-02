-- Write a SQL query to report the first name, last name,
city and state of each person in the Person table. If there is no address
for a person, report null instead.
--175 https://leetcode.com/problems/combine-two-tables/
-- Table: Person
-- +------------+---------+
-- | Column Name | Type    |
-- +------------+---------+
-- | personId   | int     |
-- | firstName  | varchar |
-- | lastName   | varchar |
-- +------------+---------+
-- personId is the primary key for this table.
-- Table: Address
-- +------------+---------+
-- | Column Name | Type    |
-- +------------+---------+
-- | addressId  | int     |
-- | personId   | int     |
-- | city       | varchar |
-- | state      | varchar |
-- +------------+---------+
-- addressId is the primary key for this table.
# passed 2-Apr-2026
SELECT pr.firstName as firstName, pr.lastName as lastName, ad.city as city, ad.state as state
from Person as pr left join Address as ad on pr.personId = ad.personId

-- 176 https://leetcode.com/problems/second-highest-salary/
-- Write a SQL query to get the second highest salary from the Employee table.
-- Table: Employee
-- +-------------+---------+
-- | Column Name  | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | salary      | int     |
-- +-------------+---------+
-- id is the primary key for this table.
-- Note: If there is no second highest salary, the query should return null.

# passed 2-Apr-2026
SELECT IFNULL((SELECT DISTINCT E.SALARY AS SecondHighestSalary FROM EMPLOYEE AS E ORDER BY E.SALARY DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
-- Service If SQl statement  - SELECT COUNT(*) FROM EMPLOYEE - to check if there is more than 1 employee in the table, if there is more than 1 employee then return 7 else return null
-- SELECT IF((SELECT COUNT(*) FROM EMPLOYEE) > 1, 7, NULL) AS E


-- 177 related to 176
-- https://leetcode.com/problems/nth-highest-salary/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE calc_ofset INT;
  SET calc_ofset = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((SELECT DISTINCT E.SALARY AS SecondHighestSalary FROM EMPLOYEE AS E ORDER BY E.SALARY DESC LIMIT 1 OFFSET calc_ofset), NULL) AS SecondHighestSalary
  );
END
