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

# PASSED 5-Apr-2026

-- 183 https://leetcode.com/problems/customers-who-never-order/
# Write a SQL query to find all customers who never order anything.
# Table: Customers
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key for this table.
# Table: Orders
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | customerId  | int     |
# +-------------+---------+
# id is the primary key for this table.
SELECT CU.NAME AS CUSTOMERS
FROM CUSTOMERS AS CU LEFT
JOIN ORDERS AS OD ON CU.ID = OD.CUSTOMERID
WHERE OD.CUSTOMERID IS NULL

--184 https://leetcode.com/problems/department-highest-salary/
# Write a SQL query to find the highest salary of each department.
# Table: Employee
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | departmentId | int     |
# +-------------+---------+
# id is the primary key for this table.
# Table: Department
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key for this table.
SELECT D.NAME AS Department, FD.Employee, FD.SALARY FROM
    (
    SELECT E.DEPARTMENTID, E.NAME AS Employee, E.SALARY as Salary FROM EMPLOYEE AS E LEFT JOIN
        (
        SELECT MAX(EM.SALARY) AS 'SALARY', EM.DEPARTMENTID FROM EMPLOYEE AS EM GROUP BY EM.DEPARTMENTID
        ) AS HS ON HS.DEPARTMENTID = E.DEPARTMENTID
        WHERE E.SALARY = HS.SALARY
    ) AS FD LEFT JOIN DEPARTMENT AS D ON D.ID = FD.DEPARTMENTID

--196 https://leetcode.com/problems/delete-duplicate-emails/ PASSED 8-Apr-2026
# Write a SQL query to delete all duplicate email entries in a table named Person, keeping only the entry with the smallest id.
# Table: Person
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key for this table.

DELETE P1 FROM PERSON AS P1
JOIN PERSON AS P2
ON P1.ID > P2.ID AND P1.EMAIL = P2.EMAIL

--197 https://leetcode.com/problems/rising-temperature/description/ passed 19-Apr-2026
# Write a SQL query to find all dates' Ids with higher temperatures compared to the previous day.
# Table: Weather
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | Id          | int     |
# | RecordDate  | date    |
# | Temperature  | int     |
# +-------------+---------+
# Id is the primary key for this table.
# Write your MySQL query statement below
-- SELECT W1.ID AS Id, W1.RECORDDATE, W2.RECORDDATE AS R2, W1.TEMPERATURE, W2.TEMPERATURE AS T2 FROM WEATHER W1
--     LEFT JOIN WEATHER W2 ON W1.RECORDDATE = W2.RECORDDATE+1
--     WHERE W1.TEMPERATURE > W2.TEMPERATURE

SELECT W1.ID AS Id FROM WEATHER W1
    LEFT JOIN WEATHER W2 ON W1.RECORDDATE = W2.RECORDDATE + 1
    WHERE W1.TEMPERATURE > W2.TEMPERATURE

failed for
| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2015-01-31 | 10          |
| 2  | 2015-02-01 | 25          |
| 3  | 2015-02-03 | 20          |
| 4  | 2015-02-04 | 30          |
expected output
| id |
| -- |
| 2  |
| 4  |

Output
| Id |
| -- |
| 4  |

Worked version:

SELECT W1.ID AS Id FROM WEATHER W1
    JOIN WEATHER W2
    ON W1.RECORDDATE = DATE_ADD(W2.RecordDate, INTERVAL 1 DAY) -- better performance
    -- ON DATEDIFF(W1.RecordDate, W2.RecordDate) = 1
    WHERE W1.TEMPERATURE > W2.TEMPERATURE

-- 511 https://leetcode.com/problems/game-play-analysis-i/description/ passed 25-Apr-2026
-- Write a solution to find the first login date for each player.
-- Table: Activity
-- +-------------+---------+
-- | Column Name  | Type    |
-- +-------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | game_played  | varchar |
-- +-------------+---------+

SELECT A.PLAYER_ID, MIN(A.EVENT_DATE) AS FIRST_LOGIN
FROM ACTIVITY A
GROUP BY A.PLAYER_ID


-- 584 https://leetcode.com/problems/find-customer-referee/description/ 1-MAY-2026 PASS
--table: Customer
--
--+-------------+---------+
--| Column Name | Type    |
--+-------------+---------+
--| id          | int     |
--| name        | varchar |
--| referee_id  | int     |
--+-------------+---------+
--In SQL, id is the primary key column for this table.
--Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
SELECT C.NAME FROM CUSTOMER C WHERE C.REFEREE_ID IS NULL OR C.REFEREE_ID != 2



