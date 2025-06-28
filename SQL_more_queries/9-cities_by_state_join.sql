-- This script lists all cities contained in the database hbtn_0d_usa, showing their ID, name, and corresponding state name.
-- As a Holberton student, I'm learning to join tables to retrieve related data.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
