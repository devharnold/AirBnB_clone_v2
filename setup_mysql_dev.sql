-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db
DROP DATABASE IF EXISTS "hbnb_dev" @ "localhost";
CREATE USER "hbnb_dev" @ "localhost" IDENTIFIED BY "hbnb_dev_pwd"
GRANT PRIVILEGES ON 'hbnb_dev_db'. * TO 'hbnb_dev' @ 'localhost'
GRANT SELECT ON 'perfomance_shema' * TO 'hbnb_dev'
FLUSH PRIVILEGES;