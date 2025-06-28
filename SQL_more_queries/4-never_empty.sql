-- This script creates the table 'id_not_null' on my MySQL server.
-- As a Holberton student, I'm learning about setting default values for columns.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
