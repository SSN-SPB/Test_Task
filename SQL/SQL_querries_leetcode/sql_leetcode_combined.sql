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

--577 https://leetcode.com/problems/employee-bonus/description/ passed 9-MAY-2026
-- Table: Employee
-- +-------------+---------+
-- | Column Name  | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | departmentId | int     |
-- +-------------+---------+
-- id is the primary key for this table.
--Table: Bonus
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| empId       | int  |
--| bonus       | int  |
--+-------------+------+
--empId is the column of unique values for this table.
--empId is a foreign key (reference column) to empId from the Employee table.
--Each row of this table contains the id of an employee and their respective bonus.
--
--Write a solution to report the name and bonus amount of each employee who satisfies either of the following:
--
--The employee has a bonus less than 1000.
--The employee did not get any bonus.
--Return the result table in any order.

SELECT E.NAME, B.BONUS
    FROM EMPLOYEE E LEFT JOIN BONUS B ON E.EMPID = B.EMPID
        WHERE B.BONUS < 1000 OR B.BONUS IS NULL

-- 585 https://leetcode.com/problems/investments-in-2016/description/ PASSED 17-MAY-2026
# Write your MySQL query statement below
SELECT ROUND(SUM(S.TIV_2016), 2) AS tiv_2016 FROM
    (
    SELECT I2.PID, I2.TIV_2016 FROM INSURANCE I2 WHERE
        I2.TIV_2015 IN
        (
        SELECT I1.TIV_2015 FROM
            (
            SELECT I.PID, I.TIV_2015, COUNT(I.TIV_2015) AS T5
            FROM INSURANCE I  GROUP BY I.TIV_2015
            ) AS I1 WHERE I1.T5 > 1
        )

        AND I2.PID NOT IN
        (
        -- find not unique location (repeated latitude & longitude)
        SELECT I4.PID FROM INSURANCE I4 RIGHT JOIN
            (
            SELECT i.lat, i.lon, COUNT(*) AS cnt
            FROM INSURANCE I
            GROUP BY i.lat, i.lon
            HAVING COUNT(*) > 1
            ) L1 ON I4.LAT = L1.LAT AND I4.LON = L1.LON
        )
    ) AS S

-- 595 https://leetcode.com/problems/big-countries/description/ passed 14-MAY-2026
--A country is big if:
--
--it has an area of at least three million (i.e., 3000000 km2), or
--it has a population of at least twenty-five million (i.e., 25000000).
--Write a solution to find the name, population, and area of the big countries.
--
--Return the result table in any order.

# Table: World
# +-------------+---------+
# | Column Name  | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | int     |
# +-------------+---------+
SELECT W.NAME, W.POPULATION, W.AREA FROM WORLD W WHERE W.AREA >= 3000000 OR W.POPULATION >= 25000000


# 602 https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/ passed 20-MAY-2026
# Write a SQL query to find the name of the person who has the most friends.
# Table: RequestAccepted
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
# (requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
SELECT RA1.ID AS id, SUM(RA1.NUM) as num FROM
(SELECT RA.requester_id AS ID, COUNT(*) AS NUM FROM RequestAccepted RA GROUP BY RA.requester_id
UNION All
SELECT RA.accepter_id AS ID, COUNT(*) AS NUM FROM RequestAccepted RA GROUP BY RA.accepter_id) RA1
GROUP BY RA1.ID ORDER BY num desc LIMIT 1

610 https://leetcode.com/problems/triangle-judgement/description/ passed 21-MAY-2026
# Write a SQL query to determine if three given sides can form a triangle.
# Table: Triangle
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| x           | int  |
--| y           | int  |
--| z           | int  |
--+-------------+------+

SELECT x, y, z, IF(X + Y > Z AND X + Z > Y AND Y + Z > X, "Yes", "No") as triangle from Triangle


# 627 https://leetcode.com/problems/swap-sex-of-employees/description/ passed 22-MAY-2026

# Write a SQL UPDATE query to swap the sex
SALARY
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+

UPDATE SALARY SET sex = IF(sex = "m", "f", "m")

626https://leetcode.com/problems/exchange-seats/description/ in progress 25/5/2026

Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.


Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
-- interim solution
SELECT S5.ID AS id, S5.SEAT as student FROM
(
SELECT S_FUL.ID, IF(S_FUL.ID%2 != 0, S1.STUDENT, S2.STUDENT ) AS SEAT FROM
Seat S_FUL INNER JOIN (SELECT S1.ID, S1.STUDENT FROM SEAT S1 WHERE S1.ID%2 = 0) S1 ON S_FUL.ID = S1.ID - 1
INNER JOIN (SELECT S2.ID, S2.STUDENT FROM SEAT S2 WHERE S2.ID%2 != 0) S2 ON S_FUL.ID = S2.ID
UNION
SELECT S_FUL1.ID, IF(S_FUL1.ID%2 = 0, S3.STUDENT, S4.STUDENT ) AS SEAT FROM
Seat S_FUL1 INNER JOIN (SELECT S3.ID, S3.STUDENT FROM SEAT S3 WHERE S3.ID%2 != 0) S3 ON S_FUL1.ID = S3.ID + 1
LEFT JOIN (SELECT S4.ID, S4.STUDENT FROM SEAT S4 WHERE S4.ID%2 != 0) S4 ON S_FUL1.ID = S4.ID
) S5 ORDER BY S5.ID

I