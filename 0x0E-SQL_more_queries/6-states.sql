-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- CREATE A TABLE IN THIS DATABASE
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
