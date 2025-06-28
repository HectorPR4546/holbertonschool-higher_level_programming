-- This script lists all the cities of California found in the database hbtn_0d_usa.
-- As a Holberton student, I'm learning to use subqueries to filter data across tables without JOINs.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
