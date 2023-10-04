- step 1:download 
	https://archive.apache.org/dist/hive/hive-2.3.4/

- step 2: extract and copy to hduser

       	sudo cp -R /home/amal/Downloads/apache-hive-2.3.4-bin ~/hive

- step 3: give directory permission

        sudo chmod -R 777 hive
- step 4: give ownership permission

      sudo chown -R hduser:hadoop hive

- step 5:
    - open bashrc file and set path

      		sudo nano ~/.bashrc

    - in the upcoming window, paste the following code

          export HIVE_HOME="/home/hduser/hive"
          export PATH="$HIVE_HOME/bin":$PATH
          export CLASSPATH=$CLASSPATH:/home/hduser/hadoop/lib/*:.
          export CLASSPATH=$CLASSPATH:/home/hduser/hive/lib/*:.

    then save

- step 6:

	execute bashrc file

	source ~/.bashrc

- step 7: then type hive 
	then hive shell will open

basic installation competed

-----------------------------------------------------------------------------------

- basic configuration

- step 1: 
    - create 3 directories user, hive, warehouse
    - these are used to store databases in hive

          	hdfs dfs -mkdir -p /user/hive/warehouse

- step 2: give permission

          hdfs dfs -chmod -R g+w /user/hive/warehouse
- step 3: change location to hive

                cd hive
- step 4:change location to conf

      	cd conf

- step 5: create file

      	sudo touch hive-site.xml

 - step 6:edit created file

      	sudo nano hive-site.xml


then paste the following content
```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>  
    <property>  
        <name>javax.jdo.option.ConnectionURL</name>  
        <value>jdbc:mysql://localhost/hcatalog?createDatabaseIfNotExist=true&amp;</value>  
    </property>
    <property>  
        <name>javax.jdo.option.ConnectionDriverName</name>  
        <value>com.mysql.jdbc.Driver</value>  
    </property>
    <property>  
        <name>javax.jdo.option.ConnectionUserName</name>  
        <value>root</value> <!--Your UserName here-->  
    </property>
    <property>  
        <name>javax.jdo.option.ConnectionPassword</name>  
        <value>Password@123</value> <!--Your MYSQL Password here-->  
    </property>
    <property>
    <name>hive.metastore.schema.verification</name>
    <value>false</value>
    </property>
    <property>
    <name>hive.exec.dynamic.partition</name>
    <value>true</value>
    </property>
    <property>
    <name>hive.exec.dynamic.partition.mode</name>
    <value>nonstrict</value>
    </property>
    <property>
    <name>hive.exec.max.dynamic.partitions</name>
    <value>1000</value>
    </property>
    <property>
    <name>hive.exec.max.dynamic.partitions.pernode</name>
    <value>1000</value>
    </property>
     <property>
    <name>hive.enforce.bucketing</name>
    <value>true</value>
    </property>
</configuration>
```

- then save the file

- step 7:then goto home

      	cd 

- step 8: copy mysql connector to hive's lib directory

        sudo cp /home/amal/Downloads/mysql-connector-java-5.1.47-bin.jar /home/hduser/hive/lib

- step 9:

	schematool -initSchema -dbType mysql

	
