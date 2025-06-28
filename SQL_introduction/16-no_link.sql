-- This script lists all records of the table 'second_table', excluding rows without a name.
-- As a Holberton student, I'm learning to handle missing data and order results.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
