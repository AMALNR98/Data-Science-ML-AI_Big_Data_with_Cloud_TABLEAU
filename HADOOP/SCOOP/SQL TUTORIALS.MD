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