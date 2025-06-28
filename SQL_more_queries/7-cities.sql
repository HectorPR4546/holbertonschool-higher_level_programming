-- This script creates the database 'hbtn_0d_usa' (if it doesn't exist) and the table 'cities' within it.
-- As a Holberton student, I'm learning about creating tables with foreign key relationships.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
