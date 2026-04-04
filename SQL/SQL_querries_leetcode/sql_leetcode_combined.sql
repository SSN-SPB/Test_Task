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


--178 https://leetcode.com/problems/rank-scores/
# Write a SQL query to rank the scores of the students,
# where the highest score gets the rank 1.
# If there are ties, assign them the same rank and skip the next ranks.
# Table: Scores
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | int     |
# +-------------+---------+
# id is the primary key for this table.

# row numbers
-- SELECT ROW_NUMBER() OVER() FROM SCORES
# row numbers with exact name
-- SELECT ROW_NUMBER() OVER() AS 'rank' FROM (SELECT ROW_NUMBER() OVER() FROM SCORES) AS SCR
# only distinct values ordered by value desc
-- Select Distinct Score as score_distinct FROM SCORES ORDER BY score_distinct DESC
# only distinct values ordered by value desc with rank
-- SELECT score_distinct as score, ROW_NUMBER() OVER() AS 'rank' FROM (Select Distinct Score as score_distinct FROM SCORES ORDER BY score_distinct DESC) as scr

SELECT SC.score, VALID_RANK.rank FROM Scores as SC
LEFT JOIN   (
    SELECT score_distinct as score, ROW_NUMBER() OVER() AS 'rank'
        FROM (Select Distinct Score as score_distinct FROM SCORES ORDER BY score_distinct DESC) as scr
            ) AS VALID_RANK ON SC.score = VALID_RANK.score ORDER BY SC.score DESC

--181 https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
# PASSED 3-Apr-2026
# Write your MySQL query statement below
-- SELECT E.* FROM EMPLOYEE AS E WHERE E.MANAGERID IS NOT NULL
-- SELECT E.* FROM EMPLOYEE AS E WHERE E.MANAGERID IS NULL
-- SELECT EM.NAME AS EMPLOYEE FROM
--     (SELECT E.* FROM EMPLOYEE AS E WHERE E.MANAGERID IS NOT NULL) AS EM
-- LEFT JOIN
--     (SELECT E.* FROM EMPLOYEE AS E WHERE E.MANAGERID IS NULL) AS MN ON MN.ID = EM.MANAGERID
--     WHERE EM.SALARY > MN.SALARY

-- SELECT MANAGERID
-- SELECT DISTINCT E.MANAGERID AS ID FROM EMPLOYEE AS E WHERE E.MANAGERID IS NOT NULL

SELECT EM.NAME AS EMPLOYEE FROM
    (SELECT E.* FROM EMPLOYEE AS E WHERE E.MANAGERID IS NOT NULL) AS EM
LEFT JOIN
    (SELECT E.* FROM EMPLOYEE AS E WHERE E.ID
        IN (SELECT DISTINCT E.MANAGERID AS ID FROM EMPLOYEE AS E WHERE E.MANAGERID IS NOT NULL)
    )
AS MN ON MN.ID = EM.MANAGERID
WHERE EM.SALARY > MN.SALARY

# PASSED 4-Apr-2026

-- 182 https://leetcode.com/problems/duplicate-emails/
# Write a SQL query to find all duplicate emails in a table named Person.
# Table: Person
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key for this table.

SELECT COUNTED.EMAIL AS EMAIL
FROM
(SELECT P.EMAIL, COUNT(P.EMAIL) AS TOTAL FROM PERSON AS P GROUP BY P.EMAIL) AS COUNTED
WHERE COUNTED.TOTAL > 1