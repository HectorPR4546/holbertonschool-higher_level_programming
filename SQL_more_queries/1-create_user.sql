-- This script creates the MySQL server user 'user_0d_1' with all privileges.
-- As a Holberton student, I'm learning about user management and permissions.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
