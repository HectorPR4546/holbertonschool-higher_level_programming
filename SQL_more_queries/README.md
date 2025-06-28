# SQL_more_queries

This directory contains SQL scripts for more advanced MySQL queries and user management tasks, as part of my Holberton School curriculum.

## Tasks Completed:

- **0-privileges.sql**: Lists all privileges for specified MySQL users.
- **1-create_user.sql**: Creates the MySQL server user `user_0d_1` with all privileges.
- **2-create_read_user.sql**: Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege on `hbtn_0d_2`.
- **3-force_name.sql**: Creates the table `force_name` with an `id` and a non-nullable `name` column.
- **4-never_empty.sql**: Creates the table `id_not_null` with an `id` column having a default value of 1, and a `name` column.
- **5-unique_id.sql**: Creates the table `unique_id` with an `id` column that has a default value of 1 and must be unique, and a `name` column.
- **6-states.sql**: Creates the database `hbtn_0d_usa` and the table `states` within it, with `id` (unique, auto-generated, primary key) and `name` (non-nullable).
- **7-cities.sql**: Creates the database `hbtn_0d_usa` and the table `cities` within it, with `id` (unique, auto-generated, primary key), `state_id` (non-nullable, foreign key to `states` table), and `name` (non-nullable).
- **8-cities_of_california_subquery.sql**: Lists all cities of California found in the `hbtn_0d_usa` database, sorted by city ID.
