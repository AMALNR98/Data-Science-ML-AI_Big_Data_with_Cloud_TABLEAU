1. show databases

	``show databases;``

2. how to create database

	``create database data_base_name;``

3. how to delete database

	``drop database database_name;``

4. select data base

	``use database_name;``
5. creation of table

	``create table table_name(schema) row format delimited fields terminated by 'data-seperation' stored as textfile;``

Here tables are imported row by row

eg:
	``create table sample1(id1 int,id2 int,id3 int,id4 int,id5 int,id6 int,id7 int) row format delimited fields terminated by ',' stored as textfile;``


  ``create table txnfile(id bigint,date_ string,customer_id bigind,price float,category string,product string,place string,street string,payment_type string) row format delimited fields terminated by ',' stored as textfile;``

6. load data to table

- here we can load from both HDFS and local at a time

	- For local
			``load data local inpath 'file-path' into table table_name;``
	
    - For HDFS
			``load data inpath 'file-path' into table table_name;``

    - this the data is stored in /user/hive/warehouse
	- when we load the data into hive the data in hdfs is 'moved into hive'
	- so the file will be removed from hdfs
	- it's a disadvantage

	- to avoid this problem


***hive tables***
----------------

internal tables vs external table??????

- 1.Internal table

	``create table table_name(schema) row format delimited fields terminated by 'data-seperation' stored as text file;``



- 2.External table
	to avoid an above problem

	``create external table table_name(schema) row format delimited fields terminated by 'data-separation' stored as text file;``



- **more HIVE queries**
-----------------

1. select particular columns

	``select column_names from table table_name;``

	- eg;
		``select id1,id2,id3 from sample1;``

2. filter data

	``select colname form table_name where condition``
	
	- eg:
		``select fname,lname,age from customer1 where age>30;``



------------------------------------------------------------------------------------------
- **VIEW TABLE**
----------------
- In hive, we can only process data
- We can't store data in HDFS.
- So we can store data in hive as table but it is not visible in HDFS, this table is known as "view table"


1. create view table
 	``create view view_table_name as query;``

	- eg:
     ``create view chennai_data as select fname,lname,age from sample4 where location=='Chennai';``


2. DROP view table

      ``drop view view_table_name;``


3. ORDER BY

	``select * from table_name order by colname asc;``

   - eg:

		``select * from sample4 order by age asc;``

   - we can also order string, small letters and block letters are seperatly sorted
		-e.g.:
     		``select * from sample4 order by fname asc;``
4. LIMIT operator

	select * from table_name limit number;

	eg:
		select * form sample4 limit 4;

	**select > count > where > order > limit**

5. DISTINCT()
	for remove duplicate rows and collect unique rows
	
	``select distinct * form table_name;``

	- eg:
		``select distinct * from customer1;``



EVALUATING FUNCTIONS
--------------------
- for perform evaluation function we have to group dataset



1. COUNT

	1. Row count
		- for row count we don't have to group data

		``select count(*) from table_name;``

		- eg: 
   			 ``select count(*) from customer1;``


   2. Each column count
		
		``select column_name, count(*) from table_name group by column_name;``

		- eg: 
		``select location, count(*) from sample4 group by location;``

```
			-----------------------------------------------------------------------------------------
			|select job, count(*) as job_count from customer1 group by job order by job_count desc;  | important example
			-----------------------------------------------------------------------------------------
		
```
2. MIN

	``select column_name, min(column_name) from table_name group by column_name;``

	- eg: 
		``select age,min(age) from customer1 group by age;``
			- *or*
		``select job,min(age) from customer1 group by job;``

3. MAX
	``select column_name,max(column_name) from table_name group by column_name;``
4. AVG
	``select coulmn_name,avg(column_name) from table_name group by column_name;``
5. SUM
	``select column_name,sum(column_name) from table_name group by coulmn_name;``


***These functions are same as MySQL queries***




Join operation
--------------

   - joining 2 tables

   - for join 2 table there should be at least 1 common field in both tables

  Type of joining:
  ---------------

  1) Inner joining
			
		- An inner join returns only the matching rows from both tables based on the specified join condition. 
		- Rows from either table that do not have a match are excluded from the result.

  - eg
		``custom :id,name,age,loc,salary ====> Table reference a b c d...``

     order1 : oid,dat,id,amount

	 we join name,age,loc,salry,dat,amount

	 so a query will

	``select c.name,c.age,c.loc,c.salary,o.dat,o.amount from custom c join order1 o on(c.id=o.id);``

   - eg:
				Steps :
                  1.	create table custom1(id int,name string, age int,loc string, salary int) row format delimited fields terminated by ',' stored as textfile;
                  2.	load data local inpath '/home/amal/Downloads/custom_employee.txt' into table custom1;
                  3.	select * from custom1;
                  4.	create table order1(oid int,dat string, id int,amount int) row format delimited fields terminated by ',' stored as textfile;
                  5.	load data local inpath '/home/amal/Downloads/order_demo.txt' into table order1;
                  6.	select * from order1;	
                  7.	select c.name,c.age,c.loc,c.salary,o.dat,o.amount from custom1 c join order1 o on(c.id=o.id);

      #first table full data, second table dat,amount

        ``select c.*, o.dat,o.amount from custom1 c join order1 o on(c.id=o.id);``
      #name,age,loc,salary,dat,amount	[salary above 3000]
        ``select c.name,c.age,c.loc,c.salary,o.dat,o.amount from custom1 c join order1 o on(c.id=o.id) where salary c.salary>3000;``


					
  2) Left outer joining
        -  A left outer join returns all the rows from the left table and the matching rows from the right table. 
        - If there is no match, NULL values are included for columns from the right table.
         

   - eg : 
		``select c.name,c.age,o.dat,o,amount from custom c left outer join order o on(c.id=o.id);``

			

  3) Right outer joining
		- A right outer join returns all the rows from the right table and the matching rows from the left table. 
		- If there is no match, NULL values are included for columns from the left table.
		-------------------------------------------------------------------------------

		- eg : 
		``select c.name,c.age,o.dat,o,amount from custom c right outer join order o on(c.id=o.id);``

  4) Full outer joining
		- A full outer join returns all the rows from both tables and includes NULL values for columns where there is no match.

        eg : 
		``select c.name,c.age,o.age,o.dat,o.amount form custom x full outer join order o on (c.id=o.id);``





Dealing with header_tag file
------------------------------

- header tags should remove when create table

	syntax:

	``create table table_name(schema) row format delimited fields terminated by ',' stored as textfile table_properties("skip.header.line.count"="1");``


