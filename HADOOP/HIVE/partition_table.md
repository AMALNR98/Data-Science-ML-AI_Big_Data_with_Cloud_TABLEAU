-HIVE PARTITION TABLE
------------------------

In Hive, a partitioned table is a table that is divided into smaller, more manageable parts based on specific partition criteria.
Partitioning allows for efficient data organization and improves query performance by reducing the amount of data that needs to be scanned.

-How to create partition table
----------------------------
- syntax:
```
CREATE TABLE my_table (
column1 datatype,
column2 datatype,
...
)		
PARTITIONED BY (partition_column1 datatype, partition_column2 datatype, ...);
```
 - eg:
          		create table table_name(id int,fname string,lname sting,age int,prog string) partitioned by (loc sting);


insert value to partition table
-----------------------------
- eg:
``
insert overwrite table partion_table_name partition(column_name) select id,fname,lname,age,prog,loc from maintable;
``

Load Data into Partitions:
-------------------------
After creating the partitioned table, you can load data into specific partitions.

- Syntax:
```			
INSERT INTO TABLE my_table PARTITION(partition_column1='value1', partition_column2=value2, ...)
VALUES (value1, value2, ...);
```
