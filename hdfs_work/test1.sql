ALTER TABLE test_sanket ADD PARTITION (name='name');


create table partioned_food_prices (name string,age int) partitioned by (age string) ;

insert overwrite table partioned_food_prices  partition(age = '2019') select series_reference, data_value, status, units, subject, product from food_prices where year='2019';

 show partitions test_sanket;


 show create table test_sanket;
 show partitions test_sanket;
ALTER TABLE test_sanket ADD PARTITION (name='value1')

CREATE TABLE employees_in_bucketed (
  ID INT,
  Name STRING,
  Age INT,
  DepartmentID INT
)
CLUSTERED BY (ID) INTO 4 BUCKETS
STORED AS ORC;

sqoop import --connect jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb --username consultants --password WelcomeItc@2022 --table office --m 1 --target-dir /tmp/sanket/



sqoop import --connect jdbc:postgresql://ec2-13-40-49-105.eu-west-2.compute.amazonaws.com:5432/testdb --username consultants --password WelcomeItc@2022  --table offices  --target-dir /warehouse/tablespace/managed/hive/sanket_user --delete-target-dir --fields-terminated-by ","  --hive-import --create-hive-table --hive-table sanket_user -m 1 --hs2-url "jdbc:hive2://ip-172-31-3-80.eu-west-2.compute.internal:10000/default;"

create table sanket_parti (sno int,usr_name string) partitioned by (name string);

insert INTO table sanket_parti (name='john Doe') select sno ,usr_name from test_sanket where name='john Doe';
-- insert value in table
INSERT INTO sanket_parti PARTITION (name='Bob')
VALUES
    (1, 'John'),
    (2, 'Alice'),
    (3, 'Bob'),
    (4, 'Emily'),
    (5, 'Michael'),
    (6, 'Sophia'),
    (7, 'David'),
    (8, 'Emma'),
    (9, 'James'),
    (10, 'Olivia');
  -- remove partiotion
  ALTER TABLE sanket_parti DROP IF EXISTS PARTITION (name='Bob');
-- craete partion
  ALTER TABLE sanket_parti ADD PARTITION (name = 'Bob');
  INSERT INTO sanket_parti (sno,name)
VALUES
    (1, 'John'),
    (2, 'Alice'),
    (3, 'Bob'),
    (4, 'Emily'),
    (5, 'Michael'),
    (6, 'Sophia'),
    (7, 'David'),
    (8, 'Emma'),
    (9, 'James'),
    (10, 'Olivia');


show create table bucket_tablename;




sqoop import --connect jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb --username consultants --password WelcomeItc@2022 --table person --m 1 --target-dir /tmp/USUK30/Sanket/import/



Create EXTERNAL TABLE usuk30.sanket_user(
    
    user_id INT,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(100),
    created_at timestamp
)
row format delimited
fields terminated by ','
stored as textfile
location '/tmp/usuk30/sanket/import';



