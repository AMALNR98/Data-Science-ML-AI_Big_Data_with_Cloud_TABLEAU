***customer1***
---------
id,fname,lname,age,prof,loc
1. age==24 ; id,fname,age,loc
2. loc == "India",fname,lname, loc,age
3. age>24 and age <50 ; fname, lname, age, prof
4. prof == 'pilot' and age>25;fname, lname,age,prof
5. age>40 and loc='india' id,fname, lname,age
6. job = pilote fname, lname, age, job
7. age > 40 and place = india fname, lname, age, job

	- ``select fname,lname,age from customer1;``
2. - ``select fname,lname,age from customer1 where age>30;``
3. - ``select id,age,lname,age,job,loc from customer1;``
4. - ``select id,fname,lname,place from customer1 where age==24;``
5. - ``select fname,lname,age,job from customer1 where age>24 AND age<50;``
6. - ``select fname,lname,age,job from customer5 where job=='pilot';``
7. - ``select fname,lname,age,job from customer1 where age>40 AND place=='india';``




***sample4.txt***
1. age mxm 2 emplyee fname, lname,age,mob
2. age minimum 1 employee fname, lname,age,loc
3. chennai work age mxm 1 employee fname,lname, age(store)

- ans:

1. ``select * from sample4 order by age desc limit 2;``
2. ``select fname,lname,age,location order by age desc limit 1;``
3. ``create view chennai_work_age_mxm as select fname,lname,age from sample4 where location=='Chennai' order by age desc limit 1;``



join
---

custom order id,name,age,loc,sal,id,date,amoutn
	- ``select c.*,o.date,o.amount from custom c join order o on(c.id=o.id) order by c.age desc limit 1;``

age max one employee full data and date and amount
	

latest date purchase name,age,loc,date,amount
	- ``select c.name,c.age,c.loc.o.dat,o.amount from custom c join order o on(c.id=o.id) order by o.dat desc limit 1;``




student and result table workout
-------------------------------
 pass name, id, res
	- ``select s.name,s.id,r.res from student s join result r on(s.id=r.id) where r.res='pass';``



1.inner join base, age > 34 candidate


Partition table
----------------

load data:
- ``create table customer(id int, fname string,lname string,age int,prog string,loc string) row format delimited fields terminated by ',' stored as textfile;``

- ``load data local inpath '.home/amal/Doucments/customer.txt' into table customer;``
- ``select * from customer;``

- ``create table par_customer(id int,fname string, lname string, age int,prog string) partitioned by(loc string);``
- ``insert overwrite table par_customer partition(loc) select id,fname,lname,age,prog,loc form customer;``

movies pandas.csv
-------------------

partition by release year of movies
