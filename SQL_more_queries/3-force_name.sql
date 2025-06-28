-- This script creates the table 'force_name' on my MySQL server.
-- As a Holberton student, I'm learning about enforcing data integrity with NOT NULL constraints.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
