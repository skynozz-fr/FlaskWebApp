CREATE DATABASE IF NOT EXISTS FlaskSql;

USE FlaskSql;

CREATE TABLE IF NOT EXISTS users (
                                   id INT AUTO_INCREMENT PRIMARY KEY,
                                   email VARCHAR(255) UNIQUE NOT NULL,
                                   password VARCHAR(255) NOT NULL
);