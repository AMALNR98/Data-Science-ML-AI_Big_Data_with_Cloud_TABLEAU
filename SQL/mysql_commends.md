


1. Create database

	- ``create database dbname;``

2. to verify the db created:

	- ``show databases;``

3. Delete database
		
	- ``drop database dbname;``

4. select database

	- ``use dbname;``	

5. create table in db

	- ``create table table_name(schema);``

	- eg:
	 	- create table sample1(col1 dtype, col2 dtype,col3 dtype...);

		- create table sample4(id int,fname varchar(20),lname varchar(30),age int,Phone_num bigint,location varchar(30));

6. to verify the table created;

	- ``show tables;``

7. describe
	- to show schema	

	- ``describe tabel_name;``

8. add colmn to mysql table
	
	- ``alter table table_name add col_name dtype;``

9. add column after an column

	- ``alter table table_name add colname dtype after colname;``

		- eg 
          - alter table employee add qualification varchar(10) after prof;

10. add column at first 
	
	- ``alter table table_name add colname dtype first;``

		- eg: 
          - alter table employee add emp_id int first;

11. at a time adding multiple columns

	- ``alter table table_name add(colname1 dtype, col2name dtype);``

	- eg: 
      - alter table employee add (state varchar(20), district varchar(20));

	- **OR**
	
	- ``alter table table_name add colname1 dtype, add colname colname2 dtype;``


12. adding multiple columns at multiple positions

	- eg:
      - alter table employee add email varchar(30) after experience, add phone_number bigint after gender;



13. how change data type

	- ``alter table table_name modify col_name  new_datatype;``

	- 	eg : 
      - alter table employee modify experience int;

14. how to change a column name

	- ``alter table table_name change old_col_name new_col_name dtype;``

	- eg: 
      - alter table employee change fname first_name varchar(20);

15. column delete

	- ``alter table table_name drop colname;``


16. to change the table name

	- ``alter table old_tablename rename to new_tablename;``

17. insert values into table

	- ``insert into table_name(colnames) values(values);``

	- eg:
      - insert into sample1(id1,id2,id3,id4,id5,id6,id7) values(102,23,14,14,203,17,18);

	- **adding  multiple values**
 		- insert into sample1(id1,id2,id3,id4,id5,id6,id7) values(12,212,232,242,232,233,232),(13,12,232,242,23,3456,4),(12,23,64,75,23,64,7,323);



18. view data from table

	- ``select * from tablename;``


**do it properly** 

19. update column value (replace)

	- ``update table_name set colname='value' where condition;``
	
	- eg : 
      - update employee set fname='athira' where id=1;


20. delete rows from table

	- ``delete from table_name where condition``

	- eg:
      - delete form employee where emp_id=110;


21. drop table

	- ``drop table table_name;``
