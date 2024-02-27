CREATE TABLE IF NOT EXISTS sanket_test (
    id INT,
    name STRING,
    age INT
);

INSERT INTO sanket_test VALUES
    (1, 'asad', 25),
    (2, 'sabastiean', 30),
    (3, 'pravith', 25),
    (4, 'elah', 30),
    (5, 'anu', 25),
    (6, 'keith', 30),
    (7, 'sanket', 28);

    SELECT * FROM sanket_test; 

    CREATE TEMPORARY TABLE sanket_test AS
SELECT 
    CASE 
        WHEN id = 1 THEN 100
        ELSE id
    END AS id,
    name,
    age
FROM my_table;

CREATE TABLE employee_records1 (
    id INT,
    name STRING,
    department STRING,
    salary INT
);

