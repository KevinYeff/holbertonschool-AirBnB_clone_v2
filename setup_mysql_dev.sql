-- Script that prepares a MySQL server for the project:

-- creating a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creating a new user in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
-- set password
IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges only for this database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant select privilege on and only performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
