create database test_bd;
use test_db;

drop table distribution_companies
create table distribution_companies(id int(10),company_name varchar(200));
insert into distribution_companies(id,company_name) values (1,'Columbia Pictures
');
INSERT INTO distribution_companies (id, company_name) VALUES
(1, 'Columbia Pictures'),
(2, 'Paramount Pictures'),
(3, 'Warner Bros. Pictures'),
(4, 'United Artists'),
(5, 'Universal Pictures'),
(6, 'New Line Cinema'),
(7, 'Miramax Films'),
(8, 'Produzioni Europee Associate'),
(9, 'Buena Vista'),
(10, 'StudioCanal');


select * from distribution_companies
CREATE TABLE movies (
    id INT PRIMARY KEY,
    movie_title VARCHAR(100),
    imdb_rating FLOAT,
    year_released INT,
    budget FLOAT,
    box_office FLOAT,
    distribution_company_id INT,
    language VARCHAR(100),
    FOREIGN KEY (distribution_company_id) REFERENCES distribution_companies(id));
    
create table distribution_companies(id int primary key,company_name varchar(1000));

insert into distribution_companies values (1,'Columbia Pictures'),(2,'Paramount Pictures'),(3,'Warner Bros. Pictures'),(4,'United Artists'),(5,'Universal Pictures'),(6,'New Line Cinema'),(7,'Miramax Films')
,(8,'Produzioni Europee Associate'),(9,'Buena Vista'),(10,'StudioCanal');

 select * from distribution_companies;
 
 
CREATE TABLE movies (
    id INT PRIMARY KEY,
    movie_title VARCHAR(100),
    imdb_rating FLOAT,
    year_released INT,
    budget FLOAT,
    box_office FLOAT,
    distribution_company_id INT,
    language VARCHAR(100),
    FOREIGN KEY (distribution_company_id) REFERENCES distribution_companies(id));
    
    
    INSERT INTO distribution_companies (id, company_name) VALUES
(1, 'Columbia Pictures'),
(2, 'Paramount Pictures'),
(3, 'Warner Bros. Pictures'),
(4, 'United Artists'),
(5, 'Universal Pictures'),
(6, 'New Line Cinema'),
(7, 'Miramax Films'),
(8, 'Produzioni Europee Associate'),
(9, 'Buena Vista'),
(10, 'StudioCanal');

  
INSERT INTO movies (id, movie_title, imdb_rating, year_released, budget, box_office, distribution_company_id, language) VALUES
(1, 'The Shawshank Redemption', 9.2, 1994, 25.00, 73.30, 1, 'English'),
(2, 'The Godfather', 9.2, 1972, 7.20, 291.00, 2, 'English'),
(3, 'The Dark Knight', 9.0, 2008, 185.00, 1006.00, 3, 'English'),
(4, 'The Godfather Part II', 9.0, 1974, 13.00, 93.00, 2, 'English, Sicilian'),
(5, '12 Angry Men', 9.0, 1957, 0.34, 2.00, 4, 'English'),
(6, 'Schindler''s List', 8.9, 1993, 22.00, 322.20, 5, 'English, German, Yiddish'),
(7, 'The Lord of the Rings: The Return of the King', 8.9, 2003, 94.00, 1146.00, 6, 'English'),
(8, 'Pulp Fiction', 8.8, 1994, 8.50, 213.90, 7, 'English'),
(9, 'The Lord of the Rings: The Fellowship of the Ring', 8.8, 2001, 93.00, 898.20, 6, 'English'),
(10, 'The Good, the Bad and the Ugly', 8.8, 1966, 1.20, 38.90, 8, 'English, Italian, Spanish');

select * from movies;
SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies;
SELECT
  movie_title,
  box_office
FROM movies
WHERE box_office > 300;

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies
WHERE movie_title LIKE '%Godfather%';

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies
WHERE year_released < 2001 AND imdb_rating > 9;

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies
WHERE year_released > 1991
ORDER BY year_released ASC;

select * from movies;

ALTER TABLE movies
ADD distribution_compnyid2 VARCHAR(255);

select * from movies;

INSERT INTO original_table (id, value1, value2)
SELECT id, value1 * 2, value2 * 2
FROM original_table
WHERE id = 1;

UPDATE movies
SET distribution_compnyid2 = distribution_company_id * 2;

select * from movies;

select distribution_company_id from movies;

UPDATE movies
SET distribution_compnyid2 = distribution_company_id * 2 
where distribution_company_id is not null;

ALTER TABLE movies
RENAME COLUMN budget TO email_address;

select * from movies;

ALTER TABLE movies
ADD distribution2 VARCHAR(255);


SELECT year_released
FROM movies
ORDER BY year_released ASC;

-- SELECT * DISTINCT distribution_company_id
-- FROM movies;

SELECT *
FROM employees
WHERE department_id IN (SELECT DISTINCT department_id FROM employees);
































 
