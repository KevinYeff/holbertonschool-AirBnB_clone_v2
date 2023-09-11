-- Script that prepares a MySQL server for the project

-- creating a test db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
-- set password
IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges for test db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privilege to user for performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
