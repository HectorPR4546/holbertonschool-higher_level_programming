-- This script creates the database 'hbtn_0d_usa' and the table 'states' within it.
-- As a Holberton student, I'm learning to set up databases and tables with specific constraints like auto-incrementing primary keys.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
