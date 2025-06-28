-- This script creates the table 'unique_id' on my MySQL server.
-- As a Holberton student, I'm learning about enforcing uniqueness for IDs.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
