1. Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

```sql

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[AEIOUaeiou]';
```

2. Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
```sql
select distinct CITY
from STATION
where CITY regexp '[aeiouAEIOU]$';
```

3. Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE (LEFT(CITY, 1)) IN ('a', 'e', 'i', 'o', 'u', 'A','E','I','O','U')
AND (RIGHT(CITY, 1)) IN ('a', 'e', 'i', 'o', 'u', 'A','E','I','O','U')
```
4. Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
```sql
select distinct CITY
from STATION
WHERE LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```
5. Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
```SQL
SELECT DISTINCT CITY
FROM STATION
where (RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u', 'A','E','I','O','U')
```
6. Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e','i','o','u')
OR LOWER(RIGHT(CITY, 1)) NOT IN ('a', 'e','i','o','u')
```
7. Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
```SQL
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY,1)) NOT IN ('a','e','i','o','u')
AND LOWER (RIGHT(CITY,1)) NOT IN ('a','e','i','o','u');
```
8. Query the Name of any student in STUDENTS who scored higher than Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
```sql
SELECT Name
FROM STUDENTS
WHERE Marks > 75 
ORDER BY RIGHT(Name, 3), ID;
```
9. Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
```sql
select name from Employee
order by name;
```
10. Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than 2000 per month who have been employees for less than months. Sort your result by ascending employee_id.
```sql
select name from Employee
where salary > 2000 and months < 10;
```
11. Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.
```SQL
select truncate(max(LAT_N), 4)
from station
where LAT_N < 137.2345;
```